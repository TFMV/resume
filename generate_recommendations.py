from fpdf import FPDF, XPos, YPos


class RecommendationsPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(
            auto=True, margin=20
        )  # Increased margin for better page breaks
        self.set_margins(left=15, top=20, right=15)  # Adjusted margins

    def header(self):
        if self.page_no() > 1:  # Skip header on cover page
            self.set_font("Helvetica", "I", 8)
            self.cell(
                0,
                10,
                f"Page {self.page_no()}/{{nb}}",
                align="R",
                new_x=XPos.LMARGIN,
                new_y=YPos.NEXT,
            )

    def footer(self):
        if self.page_no() > 1:  # Skip footer on cover page
            self.set_y(-15)
            self.set_font("Helvetica", "I", 8)
            self.cell(
                0, 10, "Thomas F McGeehan V - Professional Recommendations", align="C"
            )

    def add_cover_page(self):
        self.add_page()

        # Center content vertically
        self.set_y(self.h / 4)

        # Title
        self.set_font("Helvetica", "B", 24)
        self.set_text_color(44, 62, 80)
        self.cell(
            0,
            10,
            "Professional Recommendations",
            align="C",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )

        # Name
        self.ln(10)
        self.set_font("Helvetica", "B", 20)
        self.cell(
            0, 10, "Thomas F McGeehan V", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT
        )

        # Contact Info (optional - remove if not wanted)
        self.ln(20)
        self.set_font("Helvetica", "", 12)
        self.set_text_color(127, 140, 141)
        self.cell(
            0,
            8,
            "Data Architect & Technical Leader",
            align="C",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )

        # Date
        self.ln(50)
        from datetime import datetime

        self.set_font("Helvetica", "I", 11)
        self.cell(0, 10, datetime.now().strftime("%B %Y"), align="C")


def add_recommendation(pdf, name, title, text):
    # Check if there's enough space for at least the header of the recommendation
    if pdf.get_y() > pdf.h - 40:  # If less than 40mm left
        pdf.add_page()

    # Add separator line
    pdf.set_draw_color(52, 152, 219)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(5)

    # Name
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 8, name, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Title
    pdf.set_font("Helvetica", "I", 12)
    pdf.set_text_color(127, 140, 141)
    pdf.cell(0, 6, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    # Recommendation text with reduced line spacing
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(52, 73, 94)

    # Calculate text height and check for page break
    text_lines = len(text.split("\n"))
    estimated_height = text_lines * 5  # 5mm per line estimate

    if pdf.get_y() + estimated_height > pdf.h - 20:
        pdf.add_page()

    # Reduced line height from 6 to 5
    pdf.multi_cell(0, 5, text)
    pdf.ln(8)  # Reduced spacing after recommendation


# Create PDF
pdf = RecommendationsPDF()
pdf.alias_nb_pages()

# Add cover page
pdf.add_cover_page()

# Start recommendations on new page
pdf.add_page()

# Recommendations list
recommendations = [
    (
        "Gary Horn",
        "Senior Technical Consultant, MasterCard (retired)",
        """Please allow me to take this opportunity to assert my opinion of Tom McGeehan. I worked closely with Tom for several years; I felt it was a great loss to MasterCard to see him leave, and I believe it would be in the best interest of MasterCard to get him back. I would love the opportunity to work with him again, as he is one of the brightest young men with whom I have worked, in addition to being a very amiable person. Tom is an extremely capable programmer, and has often been quite innovative in his approach to projects. There is no problem he would consider unsolvable, and he frequently came up with technical solutions that I would not have thought of. Any organization with an emphasis on innovation should undoubtedly hire Tom because of his value in any position that could make use of his talents for conceiving and designing unique solutions to problems. His dozen or so patents probably speak for themselves. I also always found that Tom was a team player. If something needed to be done, he was willing to help make sure it was done. When I think of Tom, I think of the Boy Scout Law: trustworthy, loyal, helpful, friendly, courteous, kind, and so on, and it seems appropriate. He is the kind of person you would want on your team. In summary, if I had the opportunity, I would hire Tom in a minute and I wish he would return to MasterCard. If you have any questions, please contact me.""",
    ),
    (
        "Philip Wu",
        "Software Engineer - Risk Systems",
        """Tom McGeehan is the most intelligent and innovative problem solver I have worked with. His ability to develop breakthrough solutions for large-scale data systems is exceptional. I had the pleasure of collaborating with him on critical data warehouse projects at MasterCard, including those supporting the company's IPO. His expertise in algorithm development and mathematical modeling consistently led to cutting-edge solutions that drove business impact.""",
    ),
    (
        "Raegen Lang",
        "Business Leader, MasterCard Worldwide",
        """I've worked with Thomas McGeehan at Mastercard for over 6 years both as a peer and a direct manager. Tom received multiple well-deserved promotions to consultant and then to senior consultant (the highest technical level at Mastercard) during the 6 years he worked at Mastercard, because he consistently met and often far exceeded his job requirements. Tom is an enthusiastic, dedicated employee with reliable work habits. He often does not need guidance or supervision, but willingly accepts it when offered. He consistently improved his skills, and went above and beyond to do so. Tom is a team player and would always pitch in to help the team and do whatever it took to get the job done. He is also efficient in planning projects, punctual in meeting deadlines, and conscientiously adheres to company standards and guidelines. Tom is incredibly intelligent with excellent analytical, technical and communication skills. He was sought after to come up with creative and innovative solutions to highly-complex business and technical problems inside and outside the Data Warehouse and was able to create and implement several key applications and processes including some which are patented. In addition, Tom is able to effectively work with all levels of management and employees including business owners, customers, peers, junior resources and executive management. You'd be hard pressed to find an employee more motivated and dedicated than Tom and I highly recommend him as an excellent asset to any company he works for. If I can be of any further assistance, or provide you with any further information, please do not hesitate to contact me.""",
    ),
    (
        "Daniel Zagales",
        "Director of Data Engineering at 66degrees",
        """Tom was a valuable member of my team at 66degrees, serving as a Data Architect primarily responsible for leading database migration projects. Tom's expertise was leveraged in designing and developing database migration tooling. His contributions in this area have been instrumental in creating accelerators that have significantly improved our efficiency and effectiveness in data migration projects. He possesses a deep understanding of all facets of database technologies, storage, structures, movement, and excels at crafting well-thought-out and thorough solutions. Beyond his technical skills, Tom is a true asset to any team he works with. He is incredibly meticulous and detail-oriented, ensuring all aspects of a project are considered and addressed. Furthermore, his thoughtful approach and problem-solving abilities consistently led to successful project outcomes. I am confident that Tom would be a valuable addition to any team. His technical expertise, combined with his problem-solving skills and collaborative nature, make him an excellent team member.""",
    ),
    (
        "Jason Blythe",
        "Manager, Data Engineering at 66degrees",
        """I'm delighted to recommend Tom McGeehan for their exceptional expertise in Google Cloud specifically in the Data space. Throughout our time working together, Tom consistently demonstrated a profound understanding of GCP's data services and how to architect robust data solutions. His proficiency in designing data pipelines, storage solutions, and data warehouses within the GCP ecosystem is truly commendable. Tom has a keen eye for optimizing data architectures for performance, scalability, and cost-efficiency, ensuring our projects ran smoothly and effectively. Moreover, Tom exhibited excellent problem-solving skills when faced with complex data challenges, always coming up with innovative solutions that exceeded expectations. His ability to leverage Google's various tools and services, as well as his novel thought process and adaptability, showcased his versatility in tackling diverse data architecture requirements. In summary, Tom is an invaluable asset to any team looking to leverage Google Cloud for their data architecture needs. I wholeheartedly endorse them for their technical proficiency, problem-solving acumen, and dedication to delivering high-quality solutions.""",
    ),
    (
        "R.Kumar Balajii",
        "Software Engineer at Wipro",
        """It is my pleasure to recommend Thomas McGeehan for a challenging technical leadership role. I have known Thomas for 9 years and have worked with him for 5 years and would rank him as the best. He has an unusually vast knowledge of technologies, including Netezza, Hadoop, Exadata, Oracle, and Machine Learning with leadership skills which make him very unique and effective. McGeehan distinguished himself by generating exceptionally well-researched and well-written automation tools which are used broadly and frequently across MasterCard. I assert that McGeehan is extremely talented and has incredible analytical and communication skills. He would be a positive asset to any company. If I can be of any further assistance, or provide you with any further information, please do not hesitate to contact me.""",
    ),
    (
        "Norbert Kremer",
        "FinOps Consultant and Google Cloud Champion Innovator",
        """I have known Tommy since the days when we both learned about the Netezza Twinfin system. Like any of us who work in the database field for a long time, Tommy has acquired experience with many DBMSs, Netezza, Oracle, Exadata, BigQuery, AlloyDB and quite a few others. He's also worked with ELT and ETL tools like dbt, and BI tools like Looker. So, he's got "data stuff" covered. Over the years, we have kept in touch and we follow and critique each others' posts. In his insightful LinkedIn posts, you'll discover that Tommy is a creative and critical thinker on a range of subjects from certification exams, to Generative AI, to the latest database features in BigQuery. If I ask him a question on any of these topics, I know that I'll get a well-reasoned and authoritative reply. That makes him one of my most valuable colleagues.""",
    ),
    (
        "Nidhi Rajput",
        "Cloud Data Architect, Datastage",
        """Tom is the go-to person when you need someone to dive into uncharted territory and make sense of it all. Whether it's testing out new tech or finding creative solutions to complex problems, Tom is your guy. But what really sets him apart is his commendable knowledge of Google Cloud and finding elegant solutions to even the toughest problems. He's always willing to share that knowledge with others, helping them level up their own skills and tackle new challenges with confidence. If you're looking for someone who's not only a cloud wizard but also a fantastic team player, look no further than Tom.""",
    ),
    (
        "Timothy Carney",
        "Consultant at MasterCard",
        """I worked with Tom for almost a decade, at 2 different companies. He is one of the smartest people I know, and has applied that intelligence into dozens, if not hundreds, of algorithms and programs for major, global corporations. He has also been a successful leader and mentor leading large groups of offshore resources, from around the world.""",
    ),
    (
        "Jason Rutherford",
        "Owner at Model Technology Solutions",
        """I met Tom in college. Tom and I were roommates in college and after graduation. Tom is a fantastic leader and technical guru. Aside from his work ethic, he ranks alongside the smartest people I have ever known. He has a lot of great enterprise-level experience with a wide range of technologies, works well with others, and will no doubt emerge as a leader on any project. Hopefully my recommendation helps move your decision with Tom forward as I know he would be a great asset within your business.""",
    ),
    (
        "Vasudev Narayanan",
        "Principal Consultant at Wipro Technologies",
        """Tom is one of the best architects I have worked with. All his solutions were drawn upon mathematical equations which turn out to be sturdy and scalable. I am sure, whoever reviews his code will be enlightened. Tom is a great team player, and has very good interpersonal skills.""",
    ),
    (
        "Jennifer Schmitz",
        "Business Operations Systems Support Manager at Delta Dental of Missouri",
        """I had the pleasure of working with Tom on several highly complex data warehousing initiatives for our sales & marketing team in New York. When the business brainstormed on product ideas, Tom simultaneously thought through the design/code impact, suggesting efficiencies and increasing time to market. I learned a tremendous amount by working with Tom & he is someone I would highly recommend.""",
    ),
    (
        "Venkat Prasad Reddy Avatala",
        "Senior GCP Platform Engineer, 66degrees",
        """Tom does wonderful work, and always inspires me with his work commitment. I admire his work ethic and talent on multiple technologies. Thank you for being a great mentor to me.""",
    ),
    (
        "Joe Miner",
        "Web Developer at Veterans United Home Loans",
        """Tom has high technical skills as well as being a great teacher. He is always prepared with comprehensive knowledge of the given topic. His ability to understand and remember details of complex applications is astounding.""",
    ),
    (
        "Andy Barker",
        "Senior Architect at Swank Motion Pictures",
        """Tom is one of the best IT professionals I have ever worked with. He is very intelligent and provides great leadership and great solutions to very difficult problems.""",
    ),
]


# Group recommendations by company for better organization
def group_recommendations(recommendations):
    companies = {"MasterCard": [], "66degrees": [], "Other": []}

    for rec in recommendations:
        if "MasterCard" in rec[1]:
            companies["MasterCard"].append(rec)
        elif "66degrees" in rec[1]:
            companies["66degrees"].append(rec)
        else:
            companies["Other"].append(rec)

    return companies


# Group and sort recommendations
grouped_recs = group_recommendations(recommendations)

# Add company sections
for company, recs in grouped_recs.items():
    if recs:  # Only add section if there are recommendations
        # Check if new section should start on new page
        if pdf.get_y() > pdf.h - 50:  # If less than 50mm left
            pdf.add_page()

        # Add company section header
        pdf.set_font("Helvetica", "B", 16)
        pdf.set_text_color(41, 128, 185)  # Blue
        pdf.cell(
            0, 10, f"{company} Recommendations", new_x=XPos.LMARGIN, new_y=YPos.NEXT
        )
        pdf.ln(5)

        # Add recommendations for this company
        for rec in recs:
            add_recommendation(pdf, *rec)

        pdf.ln(5)

formatted_recommendations_path = "TFMV-Recommendations.pdf"
pdf.output(formatted_recommendations_path)

formatted_recommendations_path
