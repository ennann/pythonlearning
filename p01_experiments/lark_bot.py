import requests

webhook_url = ""


drink_message = {"msg_type":"interactive","card":{"elements":[{"tag":"div","text":{"content":"**The Sunnah way of drinking water through these easy steps:**\n1. Drink water with your right hand.\n2. Drink water by sitting.\n3. Start drinking water with saying Bismillah.\n4. See the water before drinking.\n5. Drink water in 3 Sips.\n6. Remove utensil from your mouth after each sip.\n6. After finishing each sip say **Alhamdulilla**.\n7. After 3 sips of drinking water, say finally **Alhamdulillahi Wasshukru lillaah**.\n","tag":"lark_md"}},{"alt":{"content":"","tag":"plain_text"},"img_key":"img_v2_da6791ff-9392-4b30-89a1-0f76146988bg","mode":"fit_horizontal","tag":"img"}],"header":{"template":"green","title":{"content":"Time to Drink Water!!!","tag":"plain_text"}}}}
drink_simple = {"msg_type":"interactive","card":{"elements":[{"elements":[{"content":"多喝热水，重启试试。","tag":"plain_text"}],"tag":"note"}],"header":{"template":"blue","title":{"content":"🍵 #Time to Drink Water.","tag":"plain_text"}}}}
message = {"msg_type":"interactive","card":{"elements":[{"tag":"div","text":{"tag":"lark_md","content":"<at id=all></at>\n本周会议室上下线清单，请各位查收并通知站点同学，谢谢。\n"}},{"tag":"action","actions":[{"tag":"button","text":{"tag":"plain_text","content":"查看详情"},"type":"primary","url":"https://bytedance.feishu.cn/sheets/shtcnhKKdbWShAF0w5BOUZUZBAX"}]}]}}
cr = {"msg_type":"interactive","card":{"elements":[{"tag":"markdown","content":"<at id=all></at> 本周会议室上下线清单，请各位查收并通知站点同学，谢谢。\nPS：*注意文档最近修改时间。*"},{"tag":"action","actions":[{"tag":"button","text":{"tag":"plain_text","content":"查看表格"},"type":"primary","url":"https://bytedance.feishu.cn/sheets/shtcnhKKdbWShAF0w5BOUZUZBAX"}]}],"header":{"template":"blue","title":{"content":"🎦 会议室上下线提醒","tag":"plain_text"}}}}

requests.post(webhook_url, json=drink_simple)
