import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.bgcolor = ft.colors.BLACK
    
    image = ft.Container(
        border_radius=ft.border_radius.vertical(top=20),
        clip_behavior=ft.ClipBehavior.NONE,
        width=400,
        expand=2,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.BLACK, ft.colors.PURPLE_300],
        ),
        content=ft.Image(
            src='kisspng-clash-of-clans-clash-royale-video-game-youtube-5adcb9bd2fc0b8.6439623515244149091956.png',
            scale=ft.Scale(scale=1.3)           
        )
    )
    
    info = ft.Container(
        padding=ft.padding.all(30),
        expand=2,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='LEVEL 4', color=ft.colors.PURPLE),
                ft.Text(
                    value='P.E.K.K.A.', 
                    color=ft.colors.BLACK,
                    size=40,
                    weight=ft.FontWeight.BOLD),
                ft.Text(
                    value='A P.E.K.K.A. é uma tropa lenta, e tropas lentas geralmente tem uma vida muito alta e um dano alto também, ou seja a P.E.K.K.A. é uma ótima tropa tanque e boa para ser usada em arenas maiores.'
                )
            ]
        )
    )
    
    skills = ft.Container(
        expand=1,
        bgcolor=ft.colors.PURPLE_700,
        padding=ft.padding.symmetric(horizontal=20),
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='40',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Text(
                            value='DEFESA',
                            color=ft.colors.WHITE,
                        )
                    ]
                ),
                
                ft.VerticalDivider(opacity=0.5),
                
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='8',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Text(
                            value='VELOCIDADE',
                            color=ft.colors.WHITE,
                        )
                    ]
                ),
                
                ft.VerticalDivider(opacity=0.5),
                
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='450',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Text(
                            value='DANO',
                            color=ft.colors.WHITE,
                        )
                    ]
                ),
            ]
        )
    )
    
    layout = ft.Container(
        height=700,
        width=400,
        clip_behavior=ft.ClipBehavior.NONE,
        shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.PURPLE),
        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                skills,
            ]
        )
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target = main)