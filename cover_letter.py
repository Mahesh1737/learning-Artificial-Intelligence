from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# PDF output path
pdf_file_path = "Mehesh_More_Full_Stack_Engineer_Cover_Letter_METRO.pdf"

# Create document
doc = SimpleDocTemplate(pdf_file_path, pagesize=A4,
                        rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)

# Styles
styles = getSampleStyleSheet()
style_normal = styles['Normal']
style_bold = ParagraphStyle('Bold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=12)
style_heading = ParagraphStyle('Heading', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14, spaceAfter=20)

# Cover letter content
story = []

story.append(Paragraph("Mehesh More", style_bold))
story.append(Paragraph("Email: maheshmore1737@gmail.com", style_normal))
story.append(Paragraph("Phone: 8329904289", style_normal))
story.append(Spacer(1, 20))

story.append(Paragraph("October 1, 2025", style_normal))
story.append(Spacer(1, 20))

story.append(Paragraph("Hiring Manager", style_normal))
story.append(Paragraph("METRO Global Solution Center IN", style_normal))
story.append(Spacer(1, 20))

story.append(Paragraph("<b>Subject:</b> Application for Full Stack Engineer Position", style_normal))
story.append(Spacer(1, 20))

story.append(Paragraph("Dear Hiring Manager,", style_normal))
story.append(Spacer(1, 10))

cover_text = """
I am writing to express my interest in the Full Stack Engineer position at METRO Global Solution Center IN. 
With a strong foundation in Java development, Spring Boot, and front-end technologies, combined with hands-on 
experience in building scalable web applications, I am confident in my ability to contribute effectively to your team.

During my academic and professional journey, I have developed expertise in backend development using Java, Spring Boot, 
and JPA, and have also honed my skills in front-end technologies such as React, HTML, CSS, and JavaScript. I have successfully 
designed and implemented projects that integrate RESTful APIs, database management systems, and responsive user interfaces, 
ensuring seamless performance and scalability.

I am particularly drawn to METRO Global Solution Center IN due to its commitment to innovation and high-quality software solutions. 
I thrive in collaborative environments where problem-solving and continuous learning are encouraged, and I am eager to bring my 
technical skills, analytical thinking, and passion for development to your team.

I would welcome the opportunity to discuss how my experience and skills can align with your objectives. Thank you for considering 
my application. I look forward to the possibility of contributing to METRO Global Solution Center IN as a Full Stack Engineer.
"""

story.append(Paragraph(cover_text, style_normal))
story.append(Spacer(1, 20))

story.append(Paragraph("Sincerely,", style_normal))
story.append(Spacer(1, 10))
story.append(Paragraph("Mehesh More", style_bold))

# Build PDF
doc.build(story)

print(f"PDF generated at {pdf_file_path}")