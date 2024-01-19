## Flask Application Design for "Teach more about Siberia"

### HTML Files
- **index.html**: Serves as the landing page of the application.
  - Contains basic information about Siberia, such as a brief overview, location, and key facts.
  - Includes links to other pages with more detailed content.
- **history.html**: Explores the history of Siberia, covering important events and eras.
  - Includes images and historical facts.
- **geography.html**: Provides an overview of Siberia's geographical features, including landscapes, rivers, and natural resources.
  - Contains maps, images, and interactive elements.
- **culture.html**: Delves into the rich cultural heritage of Siberia, focusing on unique traditions, art forms, and cuisine.
  - Includes audio clips of traditional music, recipes, and videos showcasing cultural events.
- **tourism.html**: Offers information about popular tourist destinations and activities in Siberia, including natural attractions, museums, and cultural landmarks.
  - Includes interactive maps, travel tips, and a customizable itinerary builder.
- **contact.html**: Provides a means for visitors to reach out to the application's creator or administrator.
  - Includes a contact form, email address, and social media links.

### Routes
- **@app.route('/')**: Directs the user to the landing page (`index.html`).
- **@app.route('/history')**: Loads the history page (`history.html`) to display information about Siberia's history.
- **@app.route('/geography')**: Directs the user to the geography page (`geography.html`) to explore Siberia's geographical features.
- **@app.route('/culture')**: Loads the culture page (`culture.html`), providing information on Siberia's cultural heritage and traditions.
- **@app.route('/tourism')**: Navigates to the tourism page (`tourism.html`), showcasing popular destinations and tourist activities in Siberia.
- **@app.route('/contact')**: Displays the contact page (`contact.html`) with contact information and a form for visitors to send inquiries.