# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
#To use a Snowpark COLUMN function named "col" we need to import it into our app. We'll place the import statement close to where we plan to use it. This will make more sense for beginners as they will be able to see why we imported it and how it is used. In a later lab, we'll move it up with other import statements in order to show good code organization.

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """)


name_on_order=st.text_input('Name on Smoothie:') 
st.write('The name on your Smoothie will be:',name_on_order)


#session = get_active_session() ----We don't need this part,we create a SniS
cnx=st.connection("snowflake")
session=cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

#Note that we import the function on line 11 and then edit line 14 so that we bring back only the FRUIT_NAME column instead of the whole table.
                                                                      
#Now we remove the selectbox that we wrote above after st.write, but i will write here the 
#code again to remember it
#option = st.selectbox(
   # "What is your favorite fruits?",
   # ("Banana", "Strawberries", "Peaches"),
#)

#st.write("Your favorite fruit is:", option)

#Replace this example with your own code!
  #**And if you're new to Streamlit,** check
  #out our easy-to-follow guides at
  #[docs.streamlit.io](https://docs.streamlit.io)

ingredients_list = st.multiselect(
'Choose up to 5 ingredienst:'
    , my_dataframe
    , max_selections=5
)

#We are placing the multiselect entries into a variable called "ingredients." We can then write "ingredients" back out to the screen.
#Our ingredients variable is an object or data type called a LIST. So it's a list in the traditional sense of the word, but it is also a datatype or object called a LIST. A LIST is different than a DATAFRAME which is also different from a STRING!
#We can use the st.write() and st.text() methods to take a closer look at what is contained in our ingredients LIST. 
#To clean up these empty brackets, we can add an IF block. It's called a block because everything below it (that is indented) will be dependent on the IF statement. 
if ingredients_list:
    ingredients_string=''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
        
    #st.write(ingredients_string)
    
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""

    #st.write(my_insert_stmt)
    #st.stop()
    
    time_to_insert=st.button('Submit Order')
    
    if time_to_insert:
        session.sql(my_insert_stmt).collect()

        st.success('Your Smoothie is ordered!',icon="✅")

import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response)

#Changing the LIST to a STRING
#In order to convert the list to a string, we need to first create a variable and then make sure Python thinks it contains a string.
#We do this by setting our variable to ' ' -- which is an empty string.
#There is no space between ''
#Create the INGREDIENTS_STRING Variable (it is wriiten above in if statement)
#How a FOR LOOP Block Works
#To convert the LIST to a STRING we can add a FOR LOOP block. A FOR LOOP will repeat once FOR every value in the LIST. 
#We can use the phrase:
#for fruit_chosen in ingredients_list:
#which actually means...
#for each fruit_chosen in ingredients_list multiselect box: do everything below this line that is indented. 
#We never defined a variable named fruit_chosen, but Python understands that whatever is placed in that position is a counter for items in the list.
#So we could just as easily say: 
#for x in ingredients_list:
#or 
#for each_fruit in ingredients_list:
#The += operator means "add this to what is already in the variable" so each time the FOR Loop is repeated, a new fruit name is appended to the existing string. 
#now we will delete the st.write and st.text right after if statement
#And add space between fruits
#Build a SQL Insert Statement & Test It(upper in if)
#Insert the Order into Snowflake (upper)
#There is a problem, when we click a fruit it goes directly to orders. Therefore we put a Submit button which makes our order after select our fruits.

#The good news is that many libraries are supported in Snowflake Snowpark!  You can refer to a list of them here:  https://repo.anaconda.com/pkgs/snowflake/
#But, beware. Not all packages in the Anaconda channel for Snowpark can be used for SiS. Because of this, use the list as a starting point and then test the packages you want to use in your SiS app by typing in the import statement for the library you want to use. 
#Adding the second variable means adding a comma in between plus single quotes.
#The Streamlit Stop command is great for troubleshooting.We want to get the SQL right before the app tries to write to the database.

