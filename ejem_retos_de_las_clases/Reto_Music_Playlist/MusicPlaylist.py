class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def size(self):
        return len(self.items)


class MusicPlaylist:
    def __init__(self):
        self.playlist = Queue()

    def add_songs(self, songs):
        for song in songs:
            self.playlist.enqueue(song)

    def play_song(self):
        if self.playlist.is_empty():
            print("No songs in the playlist")
        else:
            song = self.playlist.dequeue()
            print("Now playing:", song[0])

    def play_all_songs(self):
        if self.playlist.is_empty():
            print("No songs in the playlist")
        else:
            print("Playing all songs:")
            while not self.playlist.is_empty():
                song = self.playlist.dequeue()
                print(song[0])

    def all_songs(self):
        if self.playlist.is_empty():
            print("No songs in the playlist")
        else:
            print("Songs in the playlist:")
            for song in self.playlist.items:
                print(song[0])

'''
En esta implementación, la clase Queuerepresenta la estructura de cola basada en listas.
Mientras que la clase MusicPlaylist utiliza la cola para simular la lista de reproducción musical.

El método add_songs(songs)recibe una tupla de canciones y las agrega a la lista de reproducción utilizando el método enqueuede la cola.
El método play_song()reproducir la canción en la parte frontal de la lista de reproducción utilizando el método dequeuede la cola.
El método play_all_songs()para reproducir todas las canciones en la lista de reproducción utilizando un bucle whilehasta que la lista de reproducción esté vacía.
El método all_songs()muestra todas las canciones en la lista de reproducción utilizando el atributo itemsde la cola.
Ten en cuenta que las canciones se reproducen en el orden en que se agregan a la lista de reproducción, siguiendo el principio FIFO (First In, First Out).

Espero que esto te ayude a desarrollar el simulador de playlist musical utilizando la 
estructura Queue basada en listas en Python. Si tienes más preguntas, no dudes en preguntar.'''


#Implementacón 

# Crear una instancia de la clase MusicPlaylist
my_playlist = MusicPlaylist()

# Agregar canciones a la playlist
songs = [("Song 1", "3:45"), ("Song 2", "4:20"), ("Song 3", "2:55")]
my_playlist.add_songs(songs)

# Visualizar todas las canciones en la playlist
my_playlist.all_songs()

# Reproducir una canción
my_playlist.play_song()

# Reproducir todas las canciones en la playlist
my_playlist.play_all_songs()
