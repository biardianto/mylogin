import flet as ft


def main(page: ft.Page):
    page.title="Login and Register..."
    
    
    
    login = ft.Container(
        width=350,
        height=750,
        bgcolor="#ffffff",
        border_radius=10,
        content = ft.Column(
            width=320,
            controls=[
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=170,right=10,top=10),
                    content=ft.TextButton(
                        "Create Account",
                        style=ft.ButtonStyle(
                            color="#000000"
                        ),
                    )
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=10,right=10,top=10)
                )
            ]
        ),
    )
    signup = ft.Container(
        width=350,
        height=750,
        bgcolor="#ffffff",
        border_radius=10,
        content = ft.Column(
            
        ),
    )
    
    
    body = ft.Container(
        width = 1000,
        height = 800,
        content = ft.Row(controls=[
            login,
            signup
        ])
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
