import pygame
import random

# Inisialisasi pygame
pygame.init()

# Konstanta warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Kelas pesawat pemain
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - 50

    def update(self):
        # Menggerakkan pesawat pemain
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Batasan area pergerakan pemain
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - 50:
            self.rect.x = SCREEN_WIDTH - 50

    def shoot(self):
        # Membuat peluru baru
        bullet = Bullet(self.rect.x + 20, self.rect.y)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Kelas peluru
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Menggerakkan peluru ke atas
        self.rect.y -= 5
        if self.rect.y < 0:
            self.kill()

# Inisialisasi layar
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Game Tembak-Tembakan")

# Grup semua sprite
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Menambahkan pesawat pemain ke grup sprite
player = Player()
all_sprites.add(player)

# Variabel kontrol perulangan
running = True

# Perulangan utama game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Menembak saat tombol spasi ditekan
                player.shoot()

    # Update sprite
    all_sprites.update()

    # Deteksi tabrakan antara peluru dan pesawat pemain
    hits = pygame.sprite.spritecollide(player, bullets, False)
    if hits:
        running = False

    # Menggambar elemen game
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Memperbarui tampilan layar
    pygame.display.flip()

# Menutup pygame
pygame.quit()
