class SoundEquipment:
    def switch_on(self):
        self.state = True

    def switch_off(self):
        self.state = False

class Microphone(SoundEquipment):
    def __init__(self, volume, state=True):
        self.volume = volume
        self.state = state


    def adjust_volume(self,new_volume):
        if 0<=new_volume<=10:
            self.volume=new_volume
            print(f'Volume is now {self.volume}')
        else:
            print('Некорректный уровень громкости')

class Speaker(SoundEquipment):
    def __init__(self, bass , state=True):
        self.bass = bass
        self.state = state
    def adjust_bass(self,new_bass):
        if 0 <= new_bass <= 10:
            self.bass = new_bass
            print(f'Bass level is now {self.bass}')
        else:
            print('Некорректный уровень басса')