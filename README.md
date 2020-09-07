# aliddns

AccessKeyId以及AccessKeySecret都是在需要在阿里云控制台上获取的
domain是需要修改的域名 例如baidu.com
record_prefix 为需要更改的记录值,例如www
region_id 默认为'cn-hangzhou',这个主要是对ECS有作用，域名解析的话用不到，但是还是要传


里面有两个aliyun的依赖包需要通过pip安装

pip install aliyun-python-sdk-core 

pip install aliyun-python-sdk-alidns

ipv4和ipv6的区别不大，只是在获取ip的时候有些许区别