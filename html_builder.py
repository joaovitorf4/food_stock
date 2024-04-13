class HTMLBuilder:
    def __init__(self, items):
        self._items = items

    def build_html(self):
        self._sort_items_by_time_to_end()
        evenOrOdd = 0
        if not self._items:
            return "<html><body><p>The diet is empty.</p></body></html>"
        else:
            html_content = """
            <html>
            <head>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&display=swap" rel="stylesheet">
                <style>
                    * {
                        text-align: center;
                        font-family: "Courier New", Monospace;
                        font-weight: 900;
                        color: #000000; /* Ensuring text color is black for light mode */
                    }

                    .odd {
                        background-color: #D9E6D6; /* Light green */
                    }

                    .even {
                        background-color: #F3F8F2; /* Light gray */
                    }

                    td, th {
                        border: 0;
                        border-collapse: collapse;
                        border-spacing: 0;
                        background-image: none;
                        min-width: 12vw;
                    }

                    .main {
                        background-color: #FEF5ED; /* Light yellow */
                        border-radius: 20px;
                        padding: 60px 30px;
                    }

                    table {
                        margin: auto;
                        margin-top: 3vh;
                        margin-bottom: 3vh;
                    }
                </style>
            </head>
            <body>
                <div class="main">
                    <h2>Diet Update</h2>
                    <table>
                        <tr class="odd">
                            <th>Name</th>
                            <th>Quantity</th>
                            <th>Portion</th>
                            <th>Time to End</th>
                        </tr>
            """
            for food in self._items:
                row_class = "even" if evenOrOdd % 2 == 0 else "odd"
                html_content += f"""
                <tr class="{row_class}">
                    <td>{food.name}</td>
                    <td>{food.qtd}{food.tipo_arm}</td>
                    <td>{food.portion}{food.tipo_arm}</td>
                    <td>{food.time_to_end} days</td>
                </tr>
                """
                evenOrOdd += 1
            html_content += """
                    </table>
                </div>
            </body>
            </html>
            """
            return html_content

    def _sort_items_by_time_to_end(self):
        self._items.sort(key=lambda x: x.time_to_end)
