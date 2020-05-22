import boto3


def init():
    session = boto3.Session(
        aws_access_key_id='AKIAS3HUZYNZQG7SMBZS',
        aws_secret_access_key='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'
    )
    return session


if __name__ == '__main__':
    session = init()
    client = session.client('route53domains')
    print(client.get_domain_detail(DomainName='shricharak.com'))
    print(client.list_domains())
