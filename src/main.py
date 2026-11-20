import asyncio
from pygame import init, display, time, event, QUIT, quit
from Game import MainGame

async def main():
    init()

    screen = display.set_mode((800, 600))
    display.set_caption("Freaky Snake")
    clock = time.Clock()
    running = True

    MainGame.start()

    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
            else:
                MainGame.event()

        screen.fill("white")

        MainGame.update()

        display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

    quit()


if __name__ == "__main__":
    asyncio.run(main())