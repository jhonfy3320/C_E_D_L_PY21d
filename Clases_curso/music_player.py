'''from random import randint
from node_based_queue import Queue
from time import sleep  

class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 6)
    
    class MediaPlayerQueue(Queue):
        def __init__(self):
            super(MediaPlayerQueue, self).__init__()

        def add_track(self, track):
            self.enqueue(track)

    def play(self):
        print(f'cout: {self.cuount}')

        while self.count > 0 and self.head is not None:
            current_trac_node = self.dequeue()
            print(f'Now playing {current_trac_node}') 

            eleep(current_trac_node.head)'''



'''from random import randint
from node_based_queue import Queue
from time import sleep

class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 6)

class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        print(f"count: {self.count}")
        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f"Now playing {current_track_node.data.title}.")

            sleep(current_track_node.data.length)
            media_queue = MediaPlayerQueue()
            track = Track("Song Title")
            media_queue.add_track(track)'''

from random import randint
from node_based_queue import Queue
from time import sleep

class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 6)

class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        if isinstance(track, Track):
            self.enqueue(track)
        else:
            raise TypeError("Only Track objects can be added to the queue.")

    def play(self):
        print(f"count: {self.count}")
        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f"Now playing {current_track_node.data.title}.")

            sleep(current_track_node.data.length)


'''Python 3.10.9 (main, Mar  1 2023, 18:23:06) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from music_player import Track, MediaPlayerQueue
>>> track1 = Track("Higway to hell")
>>> track2 = Track("go")
>>> track2 = Track("Light years")
>>> track3 = Track("Heartbreaker")
>>> track4 = Track("Breath me")
>>> track5 = Track("How to dissappear completaly")
>>> my_queue = MediaPlayerQueue()
>>> my_queue.add_track(track1)
>>> my_queue.add_track(track2)
>>> my_queue.add_track(track2)
>>> my_queue.add_track(track3)
>>> my_queue.add_track(track4)
>>> my_queue.add_track(track5)
>>> my_queue.play()
count: 6'''
