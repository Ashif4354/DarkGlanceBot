import imgkit

# Set the options for conversion
options = {
    'format': 'png',
    
    'crop-h': '500',
    'quality': '100'
}

# Read the HTML file and convert it to an image
with open('page2.html') as f:
    imgkit.from_file(f, 'example.png', options=options)
