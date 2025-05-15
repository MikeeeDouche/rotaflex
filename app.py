from flask import Flask, render_template, request
from flask import render_template, redirect, url_for, flash
from forms import QuoteRequestForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rotaflex'



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = QuoteRequestForm()
    if form.validate_on_submit():
        # Extract form data
        name = form.name.data
        phone = form.phone.data
        project_type = form.project_type.data
        message = form.message.data
        
        # Optional: save to DB or send email here

        flash("Thank you for reaching out! We'll get back to you shortly.", "success")
        return redirect(url_for('contact'))  # Prevent duplicate submission
    return render_template('contact.html', form=form)

@app.route("/equipment")
def equipment():
    return render_template("equipment.html")

@app.route("/portfolio")
def portfolio():
    projects = [
        {
            'id': 1,
            'title': 'Maresca Home (Davao Del Norte)',
            'description': 'Strong and sustainable housing by NHA',
            'image': 'project1.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 2,
            'title': 'Fountain Of Beauty Residences (Camarines Sur)',
            'description': 'Safe, resilient communities provided by NHA',
            'image': 'project2.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 3,
            'title': 'NHA Housing Program 700 Units (Caluya, Antique)',
            'description': 'Empowering lives through decent shelter',
            'image': 'project3.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 4,
            'title': 'NHA Housing Program 672 Units (Burauen, Leyte)',
            'description': 'Safe, resilient communities provided by NHA',
            'image': 'project4.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 5,
            'title': 'NHA Housing Program 672 Units (Kawayan, Biliran)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project5.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 6,
            'title': 'NHA Housing Program 760 Units (TabonTabon, Leyte) Site 1',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project6.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 7,
            'title': 'NHA Housing Program 760 Units (TabonTabon, Leyte) Site 2',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project7.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 8,
            'title': 'Villa Abrea NHA Housing Program 405 Units (Almeria, Biliran) Site 2',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project8.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 9,
            'title': 'Villa El Blanco NHA Housing Program 524 Units (Almeria, Biliran) Site 1',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project9.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 12,
            'title': 'Vista Del NHA Housing Program 522 Units (Caibiran, Biliran) ',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project12.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 13,
            'title': 'Bagumbong Residences  (Bagumbong, Caloocan City)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project13.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 14,
            'title': 'Deparo Residences  (Deparo, Caloocan City)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project14.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 15,
            'title': 'New Municipal Hall (Pandan, Antique)',
            'description': 'Procurement of Civil Work for Construction',
            'image': 'project15.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 16,
            'title': 'Panghulo - Multi Purpose Building (DPWH Project)',
            'description': 'Procurement of Civil Work for Construction',
            'image': 'project16.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 17,
            'title': 'Archival Center (Quezon City)',
            'description': 'Construction',
            'image': 'project17.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 18,
            'title': 'Quezon City Central Warehouse ',
            'description': 'Construction',
            'image': 'project18.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 14,
            'title': 'Deparo Residences  (Deparo, Caloocan City)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project14.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 15,
            'title': 'Procurement of Civil Work for Construction of New Municipal Hall (Pandan, Antique)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project15.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 16,
            'title': 'Panghulo - Multi Purpose Building (DPWH Project)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project16.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 17,
            'title': 'Construction of Quezon City Archival Center (Quezon City)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project17.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 18,
            'title': 'Construction of Quezon City Central Warehouse (Quezon City)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project18.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 19,
            'title': 'Panghulo - National High School Building (DPWH Project)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project19.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 20,
            'title': 'Construction of QC Motorpool Building (DPWH Project)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project20.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 21,
            'title': 'Repainting and Improvement of Bago Bantay Elementary School',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project21.jpg',
            'service': 'On-going Projects'
        },
        {
            'id': 22,
            'title': 'Repainting and Improvement of Esteban Abada Elementary School',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project22.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 23,
            'title': 'Repainting and Improvement of Toro Hills School',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project23.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 24,
            'title': 'Repainting and Improvement of  Rosa L Susano Elementary School',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project24.jpg',
            'service': 'Airport Horizontal Structures & Bridges'
        },
        {
            'id': 25,
            'title': 'Repainting and Improvement of Quezon City High School',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project25.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 26,
            'title': 'Rehabilitation of Local Road (Malabon City)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project26.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 27,
            'title': 'Panghulo - Multi Purpose Building (DPWH Project)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project27.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 28,
            'title': 'Improvement of Road and Drainage (Madaling Araw Street)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project28.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 29,
            'title': 'REHABILITATION OF LOCAL ROAD, BERNADETTE ST.(BRGY. HULONG DUHAT, MALABON CITY)',
            'description': 'Strengthening and resurfacing of main runway.',
            'image': 'project29.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 30,
            'title': 'ARANGA STREET  (MAKATI CITY, METRO MANILA)',
            'description': 'REHABILITATION/ UPGRADING AND DRAINAGE IMPROVEMENT',
            'image': 'project30.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 31,
            'title': 'NORA VICTORIA ST. (MALABON CITY)',
            'description': 'REHABILITATION OF ROAD',
            'image': 'project31.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 32,
            'title': 'GOV. W. PASCUAL AVE.(VICENCIO ST TO SANCIANGCO ST)',
            'description': 'REHABILITATION OF DRAINAGE SYSTEM',
            'image': 'project32.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 33,
            'title': 'KAGITINGAN ST. (PHASE II) (BRGY. MUZON, MALABON CITY)',
            'description': 'REHABILITAION OF LOCAL ROAD',
            'image': 'project33.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 34,
            'title': ' ILANGILANG CREEK CASA MILAN/SITIO SEVILLE SUBD. (QUEZON CITY)',
            'description': 'CONSTRUCTION OF GROUTED RIPRAP',
            'image': 'project34.jpg',
            'service': 'Finished Projects'
        },
        {
            'id': 35,
            'title': 'MAPUYO BRIDGE AND BILIRAN CIRCUMFERENCE ROAD',
            'description': 'REHABILITATION/RECONSTRUCTION OF MAPUYO FLOOD CONTROL',
            'image': 'project35.jpg',
            'service': 'Finished Projects'
        },
        # Add more...
    ]

    services = [
    ('fa-road', 'Finished Projects'),
    ('fa-water', 'On-going Projects')
    ]
    return render_template("portfolio.html", projects=projects,services=services)


if __name__ == '__main__':
    app.run(debug=True)
