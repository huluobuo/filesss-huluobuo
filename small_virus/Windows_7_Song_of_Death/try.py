import pygame
import sys

def main():
    pygame.init()

    # 设置全屏模式
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()

    # 设置背景颜色
    background_color = (30, 30, 30)  # 深灰色
    screen.fill(background_color)

    # 设置字体
    font = pygame.font.SysFont('Arial', 36)

    # 计算进度条的位置和大小
    progress_bar_width = screen_width * 0.6
    progress_bar_height = 50
    progress_bar_x = (screen_width - progress_bar_width) / 2
    progress_bar_y = screen_height * 0.8

    # 主循环
    running = True
    progress = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 更新进度
        progress = (progress + 1) % 101  # 模拟进度

        # 绘制进度条背景
        pygame.draw.rect(screen, (50, 50, 50), (progress_bar_x, progress_bar_y, progress_bar_width, progress_bar_height))

        # 绘制进度条前景
        pygame.draw.rect(screen, (0, 120, 215), (progress_bar_x, progress_bar_y, progress_bar_width * (progress / 100), progress_bar_height))

        # 绘制进度文本
        progress_text = font.render(f'{progress}%', True, (255, 255, 255))
        text_rect = progress_text.get_rect(center=(screen_width / 2, progress_bar_y + progress_bar_height / 2))
        screen.blit(progress_text, text_rect)

        # 更新显示
        pygame.display.flip()

        # 控制帧率
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()