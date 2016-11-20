import urllib2, urllib, json, random

password_dict = {}
address_dict = {}
contract_dict = {}

def init():
    for i in range(1,10):
	name = "user%s" % i
	password = 'password%s' % i
	password_dict[name] = password
    money = 0;


def create_user(name, password):
    url = 'http://172.30.25.74:8000/users/' + name
    data = urllib.urlencode({'faucet' : '1', 'password' : password})
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    return response.read()

def get_src():
    src_string = "contract Income { uint money; function tax() { if(money < 10000){money = money * 9/10;} else if (money < 35000) { money = money * 85/100; } else {money = money *3/4;} } function get() returns (uint retVal) { return money; } function set(uint mon) { money = mon; }}" 
    print "get_src=%s" %src_string
    return src_string

def create_contract(source_name):
    url = 'http://172.30.25.74:8000/users/%s/%s/contract' % (source_name,address_dict[source_name])
    print "url=%s" % url
    #+ destination_name +'/'+ address_dict[source_name] + '/'
    data = urllib.urlencode({'password' : password_dict[source_name], 'src' : get_src()})
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    contract_dict[source_name] = response.read()

def pay_user(user_name, contract_address, amount):
    url = 'http://172.30.25.74:8000/users/%s/%s/contract/Income/%s/call' % (user_name,address_dict[user_name], contract_address)
    print "url=%s" % url
    data = { 
	    'password':password_dict[user_name],
	    'method': "set",
	    'args' : {"mon":amount},
	    'value:' :0
	    }
    
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    rc = response.read()
    print "rc=%s" % rc


def pay_employees():
    for i in contract_dict.keys():
        randoms = random.randint(0,50000)
        pay_user(i, contract_dict[i], randoms)

def get_income():
    for i in contract_dict.keys():
        get_money(i, contract_dict[i])

def do_the_taxes():
    for i in contract_dict.keys():
        do_tax(i, contract_dict[i])


def get_money(user_name, contract_address):
    url = 'http://172.30.25.74:8000/users/%s/%s/contract/Income/%s/call' % (user_name,address_dict[user_name], contract_address)
    print "url=%s" % url
    data = { 
        'password':password_dict[user_name],
        'method': "get",
        'args' : {},
        'value:' :0
        }
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    rc = response.read()
    print "income=%s" % rc

def do_tax(user_name, contract_address):
    url = 'http://172.30.25.74:8000/users/%s/%s/contract/Income/%s/call' % (user_name,address_dict[user_name], contract_address)
    print "url=%s" % url
    data = { 
        'password':password_dict[user_name],
        'method': "tax",
        'args' : {},
        'value:' :0
        }
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    rc = response.read()
    print "money=%s" % rc
	
init()
for i in password_dict.keys():
    address_dict[i] = create_user(i, password_dict[i])

for i in password_dict.keys():
    create_contract(i);

for i in password_dict.keys():
    print "password for ", i , " is " , password_dict[i]
for i in address_dict.keys():
    print "address for ", i , " is " , address_dict[i]
for i in contract_dict.keys():
    print "contract for ", i , " is " , contract_dict[i]

pay_employees()
get_income()
do_the_taxes()
get_income()
print 'BOOM'
    

