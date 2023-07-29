from YouTubeDownloader import YouTube

def pobierz_film_youtube(url, sciezka=None):
    try:
        video = YouTube(url)
        strumien = video.streams.filter(progressive=True, file_extension='mp4').first()
        if not sciezka:
            sciezka = './downloads/' + video.title + '.mp4'
        strumien.download(sciezka)
        print("Pobieranie zakończone!")
    except Exception as e:
        print("Błąd: ", e)

if __name__ == "__main__":
    print("Wprowadź adres URL filmu na YouTube:")
    url_filmu = input().strip()
    pobierz_film_youtube(url_filmu)
