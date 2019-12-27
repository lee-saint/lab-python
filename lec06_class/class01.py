"""
클래스(class):
프로그램에서 만들려고 하는 대상(객체)이 가져야 할 속성(데이터)과 기능(함수)을 묶은 '데이터타입'

메소드(method): 클래스가 가지고 있는 함수
필드(field): 클래스가 가지고 있는 데이터(변수)
"""

# TV 소프트웨어 작성
# TV 속성(데이터): 채널, 음량, 전원
# TV 기능: 채널 변경, 음량 조절, 전원 on/off

# 전원이 켜져 있는 상황에서만 채널/볼륨이 바뀌도록
# 채널: 순환하도록 (5번까지만)
# 볼륨: 최대/최소값에 도달하면 더이상 변하지 않도록


class BasicTV:
    """
    BasicTV 클래스
    """
    max_channel, min_channel = 5, 1
    max_volume, min_volume = 5, 0

    # 생성자가 호출됐을 때 실행되는 메소드(함수)
    def __init__(self, power, channel, volume):
        print('BasicTV 생성자 호출')
        self.power = power
        self.channel = channel
        self.volume = volume

    # 클래스 내부에서 정의하는 함수: 메소드
    def powerOnOff(self):
        if self.power:  # TV가 켜져 있으면(power가 True이면)
            self.power = False  # TV를 끔
            print('TV OFF')
        else:  # TV가 꺼져 있으면
            self.power = True  # TV를 켬
            print('TV ON')

    def channelUp(self):
        if self.power:
            if self.channel < self.max_channel:
                self.channel += 1
            else:
                self.channel = self.min_channel
            print('Channel :', self.channel)

    def channelDown(self):
        if self.power:
            if self.channel > self.min_channel:
                self.channel -= 1
            else:
                self.channel = self.max_channel
            print('Channel :', self.channel)

    def volumeUp(self):
        if self.power:
            if self.volume < self.max_volume:
                self.volume += 1
            print('Volume:', self.volume)

    def volumeDown(self):
        if self.power:
            if self.volume > self.min_volume:
                self.volume -= 1
            print('Volume:', self.volume)


# 클래스 설계(정의)

# 클래스의 객체(인스턴스)를 생성해 변수에 저장
# 생성자(constructor) 호출 -> 객체(object) 생성
tv1 = BasicTV(power=False, channel=1, volume=0)
print(tv1)
print(tv1.power)
tv1.powerOnOff()  # TV 켬
tv1.channelUp()
tv1.channelDown()
tv1.channelDown()
tv1.channelUp()
tv1.volumeUp()
tv1.volumeDown()
tv1.volumeDown()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.powerOnOff()  # TV 끔
tv1.channelUp()
tv1.channelDown()
tv1.channelDown()
tv1.volumeUp()
tv1.volumeDown()
tv1.volumeDown()
print(tv1.channel)



