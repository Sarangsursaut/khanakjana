from django.shortcuts import render

# Create your views here.
def home(req):
  fav={
    'item1':{'name':'Fish Grill','des':'Bone-in fish steaks hold up really well in Biryani dishes. I like to use salmon, halibut, or kingfish steaks.','img':'Fish.jpeg'},
    'item2':{'name':'Paneer Butter Masala','des':'Creamy and rich curry made with paneer cubes in a spiced tomato gravy, perfect with naan or rice.','img':'paneerButtorMasala.jpeg'},
    'item3':{'name':'Chicken Curry','des':'A classic Indian chicken curry cooked with onions, tomatoes, and aromatic spices.','img':'ChickenCurry.jpeg'},
  }
  
  return render(req,'core/home.html',{'cont':fav})

def menu(req):
  return render(req,'core/menu.html')

def contact(req):
  return render(req,'core/contact.html')

def reservation(req):
  return render(req,'core/reservation.html')

def tracking(req):
  return render(req,'core/tracking.html')