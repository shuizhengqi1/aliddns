from aliyunsdkcore import client
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest,DescribeDomainRecordsRequest,DescribeDomainRecordInfoRequest,AddDomainRecordRequest
from subprocess import *
import json
AccessKeyId = ''
AccessKeySecret = ''
domain = ''
region_id = 'cn-hangzhou'


ip = (json.loads(Popen('curl "https://api.ipify.org?format=json"',shell=True,stdout=PIPE).stdout.read()))['ip']
def getRecord():
    cl = client.AcsClient(AccessKeyId,AccessKeySecret,region_id)
    request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    request.set_PageSize(10)
    request.set_DomainName(domain)
    response = json.loads(cl.do_action_with_exception(request))
    for record in response['DomainRecords']['Record']:
        if record['Type'] == 'A':
            return {'Value':record['Value'],'RecordId':record['RecordId']}
        else:
            pass

def addDomainRecord(ip):
    cl = client.AcsClient(AccessKeyId, AccessKeySecret, region_id)
    request = AddDomainRecordRequest.AddDomainRecordRequest()
    request.set_DomainName(domain)
    request.set_Type('A')
    request.set_Value(ip)
    request.set_RR('www')
    response = cl.do_action_with_exception(request)
    print response


def updateDomainRecord(ip,recordid):
    cl = client.AcsClient(AccessKeyId, AccessKeySecret, region_id)
    request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    request.set_RecordId(recordid)
    request.set_RR('www')
    request.set_Type('A')
    request.set_Value(ip)
    response = cl.do_action_with_exception(request)
    print response
resp = getRecord()
resp_val = resp['Value']
resp_recordid = resp['RecordId']
print resp_val
print resp_recordid


if resp_val == None and ip!='' :
    addDomainRecord(ip)
    print 'add new record'
elif resp_val != ip and ip!= '':
    updateDomainRecord(ip,resp_recordid)
    print 'update to '+ip
