from alipay import AliPay

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1nlShGWe+NSp7I+fTvwJFlgoWO9PZJTEIfzQy0q1P2mgIgLkrnSo6P/MeEVvY3Q+pxmVJyuvIUZS7t5jYbkqAE6brqV3MTeLbMjT1cx2xLI2LR3Q+K92R0doaeWMer3Lv1YwV9ZyC160HxPufUyKH0GADuOE38o0T9bqv9ouTATiIfFLtkcXl7wFpZsYhIyvWWyEFzgvwyLW6DOW0KSj1/vLAlwrjRtI+ZWpOTX6A6ruEGb4eLIBJZQDGpMReu3oC/om3ydZ/8uxZn44FwpD3qGUFyuDXZxMPhQisUbpvFqy3p9eXTcresUgBO7+v3R7Hgw26MYVSANGljaONVENUQIDAQAB
-----END PUBLIC KEY-----"""

app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA1nlShGWe+NSp7I+fTvwJFlgoWO9PZJTEIfzQy0q1P2mgIgLkrnSo6P/MeEVvY3Q+pxmVJyuvIUZS7t5jYbkqAE6brqV3MTeLbMjT1cx2xLI2LR3Q+K92R0doaeWMer3Lv1YwV9ZyC160HxPufUyKH0GADuOE38o0T9bqv9ouTATiIfFLtkcXl7wFpZsYhIyvWWyEFzgvwyLW6DOW0KSj1/vLAlwrjRtI+ZWpOTX6A6ruEGb4eLIBJZQDGpMReu3oC/om3ydZ/8uxZn44FwpD3qGUFyuDXZxMPhQisUbpvFqy3p9eXTcresUgBO7+v3R7Hgw26MYVSANGljaONVENUQIDAQABAoIBABVEtLUiarBcTnmCCJdJkREhLuca3DGqOwTv0DjIsM6YB+Q3izvtn65zZ3Bp2lDvfyMM+2iGAXj4Q1MixJI1TX/4S6H3EKnVy0K/a5phC0oYLh0tPsLai40n/Ke7tsGZPrI7ttGPF4IfIxeN33GXfH76/Nr9HvkeUS+1rVPXLA4noyzMcxSh7T2uQ0um3EXtpeiyNBCPGdANFpBua3We8g4PKKpaW8J3IBBs4E1eHe/B7AsPlRDV52b94zHPzuScJq4xdfZsBQcCgfpBZ8rXApK9XPzga9NM2iz9gjx0nYfpyeTZA1HprxHtoZpUTmfi5v+nxYva7Jp7sbPuBbv51W0CgYEA/yUUbVWUaJ89/+jliYz/gu3EaBT8zY/boZuIL1IYf7IpNFec24w5ENJ9FMSiIjKC2MbzySB2IQcM+n09DK08wJSIj318TdNZTVefjXjUa0by9hp5baL5AAW7SB1SuTxqp4ip351iNdtuLCBiHWkqk4PH7s5mKYjGMxVOR+Gzur8CgYEA1zFYj2VssPSmyu4jbAkphYI5HawoJXQyqVLu7JgEaeiPyvUnxaubfgKVTTAjr5CPulWi6+QwrdxhDb9KaP80UE0X2m3XL9IuhW5qnqIyUvMmVgzefWqRwAju4kzH4B84kfKyuKgUQs3VGaFuo3xyNLUj5QLC2impE/21Mr/gi+8CgYEAqnwNVS08+FeHZwso7StQxBy6A04aygRZHng9nFj/07upOrdcMXtV2j67o3fsWmtj8ROna/oL1O/QJUQv2dub35agVTjlKV+SqVJmY3KchX4n9HgmMTMXrIMn6/zj/LA5F+8Ci0+vgws3Z7bPuJVABMemfZRewVwKC7It12wh2yMCgYEAkps6047s6u3yyGRPW6YuVJfwo6eLPmEYtsUao7O5phHcDRDShNgyOjo2T30RguXBFdiMA5vWEk0HDh+Z6Uic8mxjaNvWc+0E5sDgAK1ODbc8Efn4hodZPvSXEzPuJGIA32Xynt1b2Ft06F5UCyuYfxI9nyMvbwRc/ZKmpSmWKJ8CgYEAvc+FUc63clnU/Sb2Sj7c2oA9UetY3adqLgIFD+tZI5+lb+XiXenNh7NYfQ4zQ0N9GGX+aiBKHDXHuZ0hJj3hcpGaz9dPUl19bzWTrUQ1Ysdo13AUQWrce0mxY6fEjosB+qnNql1abCHqyYu1nNZVWcAHE0ZT3C//eJmVyu5Ao84=
-----END RSA PRIVATE KEY-----"""

alipay = AliPay(
    appid = "2088102178923430",
    app_notify_url = None,
    app_private_key_string = app_private_key_string,
    alipay_public_key_string = alipay_public_key_string,
    sign_type= "RSA2"
)

#发起支付请求
order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no="33455", #订单号
    total_amount=str(1000),#支付金额
    subject="生鲜交易", #交易主题
    return_url=None,
    notify_url=None
)

print("https://openapi.alipaydev.com/gateway.do"+order_string)