import flet
import backend as back
import datetime
import sys

import matplotlib.pyplot as plt

def main(page: flet.Page):
    page.title = "BiteBalance - Track your calories"
    page.scroll="AUTO"
    page.fonts={"CutiveMono":"D:\\3rd Sem Mini Project\\CutiveMono-Regular.ttf"}
    #theme = flet.Theme()
    #theme.page_transitions.windows = flet.PageTransitionTheme.ZOOM
    #page.theme = theme.Theme(color_scheme_seed="green")
    #page.update()

    #Title row
    title_filler=flet.Text("",expand=3,size=30,font_family="Sans Serif",weight=flet.FontWeight.W_100)
    title_text=flet.Text("BiteBalance",expand=4,size=30,font_family="Open Sans Semibold",weight=flet.FontWeight.W_100)

    #Row 1
    food_name_field=flet.TextField(label='Enter food name to add to your meal',expand=5)
    food_id=0
    food_data=()
    def food_add_bttn_clicked(e):
    	nonlocal food_id
    	nonlocal food_data
    	food_id=back.get_food_id(food_name_field.value)
    	print(food_id)
    	if food_id!=-1 and food_id!=0:
    		food_data=back.get_food_data(food_id)
    		food_group_field.value=food_data[2]
    		calories_field.value=food_data[3]
    		fat_field.value=food_data[4]
    		protein_field.value=food_data[5]
    		carb_feild.value=food_data[6]
    		sugar_field.value=food_data[7]
    		fiber_feild.value=food_data[8]
    		page.update()
    food_add_bttn=flet.ElevatedButton(content=flet.Row([flet.Icon(flet.icons.ADD), flet.Text("  Add food here")]),expand=1, on_click=food_add_bttn_clicked)

    #Row 2
    date=""
    food_group_field=flet.TextField(expand=2,label='Food group')
    calories_field=flet.TextField(label='Calories(KCal)',expand=3)
    def date_picker_date_change(e):
    	nonlocal date
    	date=str(date_picker.value.strftime("%d,%b'%y")) #24-01-24
    	add_to_intake_bttn.disabled=False
    	page.update()
    def date_picker_date_close(e):
    	add_to_intake_bttn.disabled=True
    	page.update()
    date_picker = flet.DatePicker(
    	on_change=date_picker_date_change,
    	on_dismiss=date_picker_date_close,
        first_date=datetime.datetime(2024, 1, 1),
        last_date=datetime.datetime(2024, 1, 31),
    )
    page.overlay.append(date_picker)
    date_button = flet.ElevatedButton(
        "D A T E",
        expand=1,
        icon=flet.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
    )

    #Row 3
    fat_field=flet.TextField(label='Fat(g)',expand=2)
    protein_field=flet.TextField(label='Protein(g)', expand=1)

    #Row 4
    carb_feild=flet.TextField(expand=2,label='Carbohydrates(g)')
    sugar_field=flet.TextField(expand=1,label='Sugar(g)')
    fiber_feild=flet.TextField(expand=1,label='Fibers(g)')
    def add_to_intake_bttn_clicked(e):
    	back.update_user_data(date, calories_field.value)
    add_to_intake_bttn=flet.FloatingActionButton(expand=2,content=flet.Row([flet.Icon(flet.icons.ADD), flet.Text("Add to your intake")], alignment="center", spacing=5), bgcolor=flet.colors.INDIGO_400, shape=flet.RoundedRectangleBorder(radius=5), width=150, mini=True, on_click=add_to_intake_bttn_clicked,disabled=True)

    #Row 5
    amount_feild=flet.TextField(expand=2,label='Enter amount consumed(g)')
    def set_amount_button_clicked(e):
    	multiplier=float(amount_feild.value)
    	calories_field.value=(food_data[3]/100)*multiplier
    	fat_field.value=(food_data[4]/100)*multiplier
    	protein_field.value=(food_data[5]/100)*multiplier
    	carb_feild.value=(food_data[6]/100)*multiplier
    	sugar_field.value=(food_data[7]/100)*multiplier
    	fiber_feild.value=(food_data[8]/100)*multiplier
    	page.update()
    set_amount_button=flet.FilledButton("Set amount consumed", expand=1, icon="add", icon_color=flet.colors.INDIGO_400, on_click=set_amount_button_clicked)

    #Row 6
    user_data={}
    def track_bttn_clicked(e):
    	nonlocal user_data
    	user_data=back.get_user_data()

    	x=list(user_data.keys())
    	y=list(user_data.values())
    	plt.plot(x,y, marker='X', color ='gray', label='Calorie Intake Trend')
    	plt.legend(loc="upper left")
    	plt.title("BiteBalance Calorie Tracking", fontsize=15)
    	plt.xlabel("Date", fontsize=10)
    	plt.ylabel("Calorie Intake [ KCal ]",fontsize=10)
    	plt.show()

    track_bttn=flet.ElevatedButton(expand=1,text="Track total calorie intake",on_click=track_bttn_clicked)
    
    #Row 7
    search_food_field=flet.TextField(expand=5,label='Search for food items')
    food_search_result=list()
    #Row 7.5
    search_banner=flet.ElevatedButton(expand=1,text='Search Result:', style=flet.ButtonStyle(shape={flet.MaterialState.DEFAULT: flet.RoundedRectangleBorder(radius=5)}), disabled=True)

    already_displayed=0
    def search_bttn_clicked(e):

    	nonlocal already_displayed
    	nonlocal food_search_result
    	if search_food_field.value!="":
            food_search_result=back.get_food_list(search_food_field.value)
            if food_search_result!=-1:
                if already_displayed==0:
                    already_displayed=1
                    for food_name in food_search_result:
                        search_result_list.controls.append(flet.Text(food_name))
                    page.add(flet.Row(controls=[search_banner]), flet.SelectionArea(search_result_list))
                    page.update()
                else:
                    page.remove_at(8)
                    search_result_list.controls.clear()
                    page.update()
                    for food_name in food_search_result:
                        search_result_list.controls.append(flet.Text(food_name))
                    page.add(flet.Row(controls=[search_banner]), flet.SelectionArea(search_result_list))
                    page.update()

    search_bttn=flet.ElevatedButton(text="Search", expand=1, on_click=search_bttn_clicked)

    #Row 8
    search_result_list = flet.ListView(expand=1, divider_thickness=2, spacing=2, padding=20, auto_scroll=True)

    #app container place

    page.add(
    	flet.Row(controls=[title_filler,title_text]),
    	flet.Row(controls=[food_name_field, food_add_bttn]),
        flet.Row(controls=[food_group_field, calories_field, date_button]),
        flet.Row(controls=[fat_field, protein_field]),
        flet.Row(controls=[carb_feild, sugar_field, fiber_feild, add_to_intake_bttn]),
        flet.Row(controls=[amount_feild, set_amount_button]),
        flet.Row(controls=[track_bttn]),
        flet.Row(controls=[search_food_field,search_bttn])
        )

    page.theme = flet.theme.Theme(color_scheme_seed='indigo')
    page.update()


flet.app(target=main)