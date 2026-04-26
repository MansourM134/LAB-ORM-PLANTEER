# LAB-ORM-PLANTEER


## Using what you learned, Create a new website called "Planteer" , this website has the following pages/paths:
- Home page `/`
- All Plants page : `plants/all/`
- Plant Detail Page : `plants/<plant_id>/detail/`
- Add new plant page : `plants/new/`
- Update plant page : `plants/<plant_id>/update/`,
- Delete Plant : `plants/<plant_id>/delete/`
- Search Page : `plants/search/`
- (Bonus) Contact Us page : `contact/`
- (Bonus) Contact Us Messages page : `contact/messages/`


### Notes:
- Use templates & template inheritance.
- The website must be responsive (looks good on big and small screens)
- In all plants page, user can filter by `category` and `is_edible`.
- For the images, backgrounds, fonts you can use whatever you like. As for the content like categories,  make sure you add real plants with real plants images.
- Use at least 2 apps, one main and one for the plants.
- In Plant detail page , Add related plants (based on the same category, use filter !)
- Do frontend and backend validation. 
  
## wireframe for the main pages
<img width="1771" style="width:100%" alt="Screenshot 2024-03-19 at 2 27 18 PM" src="assets/main-wireframe.png">

## Contact pages wireframe:
<img width="1015" style="width:100%" alt="Screenshot 2024-03-19 at 3 22 17 PM" src="assets/contact-wireframe.png">


## UML for the model `Plant` &  `Contact` Model 
<img width="618" style="width:100%; height:auto;" alt="Screenshot 2024-03-19 at 3 16 01 PM" src="assets/uml.png">


## Using what you learned, Create a new model called "Comments", connect the "Plant" with the "Comment" using one to many relation:
Comment model will include:
- relation to Plant model
- name
- content
- date

# Notes
- use the right fields to each attribute
- allow the user to add a comment on a plant
- display all the comments related to a plant in the plant's page

# We want to add the countries that the plant is native to. 
For example palm tree is native to :
Saudi Arabia, Iraq, Kuwait, etc.


1. To do this you will need a new Model and a relation on the Plant model.

Model Country:
- name (Varcher)
- flag  (Image)

Model Plant:
- …
- …
- countries : relationship of type manyToMany with Country


2. We need to be able to filter by country, for example I want to be able to list all native plants to Saudi Arabia in the all plants page.

3. (Bonus): I want to be able in the detail page to click on a country, and then it displays a page with all plants native to that country.
4. (Bonus): Use include to unify the plant card across the website.

# LAB for Django Authentication:
- Add the feature of registering new users and logging in to the Planteer project.
- Link the comments that are added to users.
- Restrict the ability to add, update, and delete plants to the Admin only.
- Only registered users can add comments on a plant; otherwise, show a message prompting unregistered users to sign up in order to add a comment.
