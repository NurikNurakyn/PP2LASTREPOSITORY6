import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("MP3 Player")

MUSIC = "music"
tracks = [os.path.join(MUSIC, file) for file in os.listdir(MUSIC) if file.endswith(".mp3")]

current_track = 0
pygame.mixer.music.set_volume(0.5)

def play_track(index):
    pygame.mixer.music.load(tracks[index])
    pygame.mixer.music.play()


play_track(current_track)

running = True
paused = False

print("W-Pause/Continue > S-Stop > D-Next song > A-Previous song > Space-Pause/Continue ")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if paused:
                    pygame.mixer.music.unpause()
                    print("Continue")
                else:
                    pygame.mixer.music.pause()
                    print("Pause")
                paused = not paused

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("Stop")

            elif event.key == pygame.K_d:
                current_track = (current_track + 1) % len(tracks)
                play_track(current_track)
                print(f"Next track: {os.path.basename(tracks[current_track])}")

            elif event.key == pygame.K_a:
                current_track = (current_track - 1) % len(tracks)
                play_track(current_track)
                print(f"Previous track: {os.path.basename(tracks[current_track])}")

            elif event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    print("Continue")
                else:
                    pygame.mixer.music.pause()
                    print("Pause")
                paused = not paused

            elif event.key == pygame.K_q:
                pygame.mixer.music.rewind()
                print("Restart")

            elif pygame.K_0 <= event.key <= pygame.K_9:
                vol = (event.key - pygame.K_0) / 10
                pygame.mixer.music.set_volume(vol)
                print(f"Volume: {int(vol * 100)}")

            elif event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
