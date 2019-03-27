## 给人类看的ReadMe

>  姓名：Marcus
>
>  年龄：10岁
>
>  性格：搞怪
>
>  技能：XSS防御
>
>  朋友：Flynn(同学)
>
>  家人：Owen(父亲)

Marcus从小受到父亲Owen影响，对于**数据分析**方面有着很大的家庭影响。

但是他本人并不喜欢每天面对着一堆数据，忙忙叨叨的不知道干什么。

他真正喜欢的是信息**安全**的部分。

更是对*XSS漏洞攻击*有着自己独特的见解。

他总是跟好朋友Flynn讨论XSS攻击绕过的一些姿势，不过Flynn好像不太感冒。

于是他只能说说数据方面的事，好在Flynn还听得进去。

为了让自己的兴趣不和父亲的期望冲突，Marcus自己琢磨一套利用**机器学习算法防御XSS攻击**的手段。

但是他太爱搞怪了，有时候给他一个简简单单的字母，他也一口咬定就是XSS攻击。

真是淘气。



## ReadMe For Programmer

Marcus is a XSS Filter I write for laboratory internal sharing.

It combine the information security knowledge that I know and the machine learning algorithm that I've been study these days.

Other than a sharing,it's more like a summing up,to apply what I have learned.

But I'm really not sure if Marcus can behave well in production environment.

So,just be it.

### Usage

Run follow command in terminal

> python manage.py runserver

Bang！It‘s over。

And all you need to do is call the API and look what it says.

| URL       | http://127.0.0.1:8000/xss/ |
| --------- | -------------------------- |
| Method    | POST                       |
| Parameter | string                     |

You can refer to the images below.

### Features

Very few codes.

For anomaly detection, the biggest shortcoming is a substantial false alarm rate. 

### Requirements

django

sklearn

numpy

### Screenshots

two images during detecting xss 

![20190327150405](https://raw.githubusercontent.com/JosephTribbianni/Marcus/master/images/20190327150405.png)

![20190327150615](https://raw.githubusercontent.com/JosephTribbianni/Marcus/master/images/20190327150615.png)


