## P.E.K.K.A. Character Display with Flet

This project showcases a P.E.K.K.A. character display using the Flet framework. The display includes an image of the character, a description, and the character's skills, all styled with custom alignments, gradients, and other visual properties.

## Features

- Centered layout with a fixed minimum window size
- Gradient background and custom-styled containers
- Detailed character information including image, level, name, description, and skills
- Responsive and visually appealing design

## Installation
1. Ensure you have Python installed (preferably version 3.7 or higher).
2. Install the flet package if you haven't already:

    ```bash
    pip install flet
    ```

## Usage

1. Save the script to a file, for example, `pekka_display.py`.
2. Run the script:

    ```bash
    python pekka_display.py
    ```

## Code Overview

## Main Function

The main function is the entry point of the application. It sets up the page properties and adds the main layout container.

    ```python
    def main(page: ft.Page):
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window_min_width = 500
        page.bgcolor = ft.colors.BLACK
    ```

## Image Container

The image container displays the character's image with a gradient background and rounded top corners.

    ```python
    image = ft.Container(
        ...
        content=ft.Image(
            src='kisspng-clash-of-clans-clash-royale-video-game-youtube-5adcb9bd2fc0b8.6439623515244149091956.png',
            scale=ft.Scale(scale=1.3)           
        )
    )
    ```

## Info Container

The info container displays the character's level, name, and description.

    ```python
    info = ft.Container(
        ...
        content=ft.Column(
            controls=[
                ft.Text(value='LEVEL 4', color=ft.colors.PURPLE),
                ft.Text(
                    value='P.E.K.K.A.', 
                    color=ft.colors.BLACK,
                    size=40,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Text(
                    value='A P.E.K.K.A. é uma tropa lenta...'
                )
            ]
        )
    )
    ```

## Skills Container

The skills container displays the character's skill statistics: defense, speed, and damage.

    ```python
    skills = ft.Container(
        ...
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            value='40',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Text(
                            value='DEFESA',
                            color=ft.colors.WHITE
                        )
                    ]
                ),
                ...
            ]
        )
    )
    ```

## Layout Container

The layout container brings together the image, info, and skills containers into a cohesive design.

    ```python
    layout = ft.Container(
        ...
        content=ft.Column(
            controls=[
                image,
                info,
                skills
            ]
        )
    )
    ```

## Entry Point

The script runs the main function when executed directly.

    ```python
    if __name__ == '__main__':
        ft.app(target=main)
    ```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.