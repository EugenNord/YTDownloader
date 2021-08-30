from pytube import YouTube

link = input('Введите ссылку для скачивания - ')
yt = YouTube(link)

print('Название:', yt.title)
print('Просмотров:', yt.views)
print('Длительность:', yt.length)
#print(yt.streams)

print(yt.streams.filter(res='2160p'))
ys = yt.streams.get_by_itag(401)
ys.download('/Users/Daemon/Desktop')

print(yt.streams.filter(type='audio'))
ys = yt.streams.get_by_itag(140)
ys.download('/Users/Daemon/Desktop/11')

#  ys = yt.streams.get_highest_resolution()
#  ys.download('/Users/Daemon/Desktop')

print('Успешно')