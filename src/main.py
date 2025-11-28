import flet as ft
import Signup as sg


def main(page: ft.Page):
    page.title = "Login and Register..."

    login = ft.Container(
        width=320,
        height=750,
        bgcolor="#ffffff",
        border_radius=10,
        content=ft.Column(
            width=320,
            controls=[
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=170, right=10, top=10),
                    content=ft.TextButton(
                        "Create Account",
                        style=ft.ButtonStyle(
                            color="#000000",
                        ),
                    ),
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=110, right=10, top=3),
                    content=ft.Text(
                        "Login",
                        size=30,
                        color="#000000",
                        weight="w700",
                    ),
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=20, right=20, top=20),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        "Please enter your information below in order to login to your account",
                        size=14,
                        color="#000000",
                        text_align="center",
                    ),
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=20, right=20, top=20),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Username",
                                size=14,
                                color="#000000",
                            ),
                            ft.TextField(
                                text_style=ft.TextStyle(
                                    color="#000000",
                                ),
                                border_radius=15,
                                border_color=ft.Colors.BLACK,
                                focused_border_color=ft.Colors.ORANGE,
                            ),
                        ]
                    ),
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=20, right=20, top=5),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Password",
                                size=14,
                                color="#000000",
                            ),
                            ft.TextField(
                                text_style=ft.TextStyle(
                                    color="#000000",
                                ),
                                password=True,
                                can_reveal_password=True,
                                border_radius=15,
                                border_color=ft.Colors.BLACK,
                                focused_border_color=ft.Colors.ORANGE,
                            ),
                        ]
                    ),
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=120),
                    content=ft.TextButton(
                        "Forgot Password?", style=ft.ButtonStyle(color="#000000")
                    ),
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=20, right=20, top=20),
                    content=ft.TextButton(
                        "Login",
                        width=300,
                        height=55,
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.ORANGE_700,
                            shape={
                                ft.ControlState.FOCUSED: ft.RoundedRectangleBorder(
                                    radius=15
                                ),
                                ft.ControlState.HOVERED: ft.RoundedRectangleBorder(
                                    radius=15
                                ),
                            },
                            padding=20,
                        ),
                    ),
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=20, right=20, top=15),
                    content=ft.Text(
                        "Or use social media account.",
                        size=14,
                        text_align="center",
                        color="#000000",
                    ),
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=20, right=20, top=15),
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                ft.Image(
                                    r"img\facebook.png",
                                    width=48,
                                ),
                                margin=ft.margin.only(right=10),
                            ),
                            ft.Container(
                                ft.Image(
                                    r"img\gmail.png",
                                    width=48,
                                ),
                                margin=ft.margin.only(right=10),
                            ),
                            ft.Container(
                                ft.Image(
                                    r"img\mail.png",
                                    width=48,
                                ),
                                margin=ft.margin.only(right=10),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ),
            ],
        ),
    )
    signup = ft.Container(
        width=320,
        height=750,
        bgcolor="#ffffff",
        border_radius=10,
        content=ft.Column(
            width=320,
            controls=[
                ft.Container(
                    width=300,
                    content=ft.IconButton(
                        # icon=
                    )
                )
            ]
        ),
    )

    body = ft.Container(
        width=1000,
        height=800,
        content=ft.Row(
            controls=[
                login,
                signup,
                # sg.signupx,
            ],
        ),
    )

    page.add(body)


ft.app(target=main)


# def main(page: ft.Page):
#     counter = ft.Text("0", size=50, data=0)

#     def increment_click(e):
#         counter.data += 1
#         counter.value = str(counter.data)
#         counter.update()

#     page.floating_action_button = ft.FloatingActionButton(
#         icon=ft.Icons.ADD, on_click=increment_click
#     )
#     page.add(
#         ft.SafeArea(
#             ft.Container(
#                 counter,
#                 alignment=ft.alignment.center,
#             ),
#             expand=True,
#         )
#     )


# ft.app(main)
