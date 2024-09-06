import streamlit as st  

skill_col_size = 5

def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("🏠_Mainpage.py", label="Introduction", icon="🏠")
    bar2.page_link("pages/2_🎨_Portofolio.py", label="Portofolio", icon="🎨")
    bar3.page_link("pages/1_📚_Certificates.py", label= "Certifications", icon="📚")
    bar4.page_link("pages/3_🌏_Contacts.py", label="Contacts", icon="🌏")
    st.write("")

#publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''

# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {'brief':
              """    
                Hey there! I’m Jashesh Kanzariya, a tech enthusiast with a passion for turning ideas into reality through code. I grew up in the vibrant city of Vadodara, where my love for technology started to take root.

I’m all about diving deep into the nitty-gritty of software development, whether it’s crafting efficient algorithms, ensuring seamless integration, or exploring the latest tech trends. My expertise lies in building solutions that are not just functional but also impactful. Python is my go-to language, and I love experimenting with various frameworks to bring projects to life.
              """,
        'name':'Jashesh Kanzariya', 
        'study':'Parul University',
        'location':'Vadodara, India',
        'interest':'Python, Data Science, AI-ML',
        'skills':['Python','HTML & CSS','Streamlit','PyQT','MySQL','SQLite','Github','Figma','OpenAI API','Excalidraw'],
        }

# Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#[[header, subheader, date,]

certificates = [
    {
        "title": "Data Analytics with Python",
        "organization": "NPTEL",
        "date": "Jan-Apr 2024",
        "image": "src/2.png",
        
    },
    {
        "title": "Data Analytics and Visualization Job Simutulation",
        "organization": "Accenture",
        "date": "Sept 5th 2024",
        "image": "src/1.png",
       
    },
    {
        "title": "Python Mega Course",
        "organization": "Udemy",
        "date": "July 29, 2024",
        "image": "src/3.png",
        
    },
    {
        "title": "Build an Azure Ai Vision solution",
        "organization": "Microsoft",
        "date": "Jan 30, 2024",
        "image": "src/4.png",
        
    },
    
] 

# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
phone = "88666 70830"
blog = "https://hashnode.com/@botjash"
linkedin_link = "https://www.linkedin.com/in/jashesh-kanzariya/"
github_link = "https://github.com/jasheshK"


# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"

StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Rsirp0c/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''
