ETS简单交易系统
=============

##描述

采用Django的models模型，可以复用Django的Auth模型，实现如下：

###账号权限管理

* 账号注册，email验证、找回密码
* 登录、图片验证码
* 用户资料编辑，主要有：账号（必填）、email（必填）、状态、昵称、头像图片、QQ、微信、手机号（验证短*信）、真实姓名、证件号码、联系地址等；在线用户列表；
* 后台管理等功能，编辑用户资料、锁定账号；用户经验值、注册IP、最近登录IP、最近登录时间、累计登录次数、登录日志、操作日志、经常登录的十个IP等；功能权限管理；
* 有待进一步补充

###策略管理

* 未注册的用户，可以查看免费公开的策略，可以看到收费的策略列表；策略广场
* 已注册的用户，新建策略、编辑策略、删除策略；
* 策略搜索；
* 策略热度；支持点赞、回踩
* 策略定价、买卖
* 有待进一步补充

###好友关系管理

* 陌生人、关注、粉丝、好友等；
* 有待进一步补充


##关于我

* Email：cryhelyxx@gmail.com

* Blog：[我的CSDN博客](http://blog.csdn.net/Cryhelyxx "Cryhelyxx的挨踢博客")

* Github： [我的github](https://github.com/Cryhelyxx "Cryhelyxx的github")

Copyright © 2015 `Cryhelyxx`, All Rights Reserved
