from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    name = input("Name: ")

    pdf = PDF()
    pdf.add_page()

    # Shirt image
    pdf.image("shirtificate.png", x=10, y=50, w=190)

    # Text on shirt
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 110)
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
