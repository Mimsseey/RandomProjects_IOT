def Notify_Admin(new_data, print_items=False):
      if len(new_data)>0:
            print(f"you have new data! {len(new_data)} items!")
            if print_items:
                  for i in new_data:
                        print(i.Get_String())
      else:
            print("Nothing New..")

def Print_All_Data(data):
      for i in data:
            print(i.Get_String())
            print("************************\n")

def Make_HTML(data):
      style = "<link rel='stylesheet' type='text/css' href='style.css'>"    
      strTable = "<html>"+style+"<body><h1>Metallibord</h1><table><tr><th></th></tr>"
 
      for i in range(len(data)):
            item_id = data[i].item_id
            item_title = f"<h3><a href='https://www.google.co.il/maps/place/{data[i].title}'>{data[i].title}</a></h3>"
            item_subtitle = f"<p>{data[i].subtitle}</p>"
            item_num_spec = f"<p>rooms:{data[i].room_num}      size:{data[i].size}</p>"
            item_price = f"<h5>{data[i].price}</h5>"
            item_date = f"<p>{data[i].date}</p>"
            item_save_btn = "<input type='button' class='button' value='Save'/>"
            
            strRW = f"<tr><td dir='rtl'>"+f"{item_date}{item_title}{item_subtitle}{item_num_spec}{item_id}{item_price}{item_save_btn}"+ "</td></tr>"

            strTable = strTable+strRW

      page_script = """<script
            src="https://code.jquery.com/jquery-3.4.1.min.js"
            integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
            crossorigin="anonymous"></script>
            <script>
            $(function(){
            $(".button").click(function(e){
            data={"message": $(e.target).parent().text()}
            $.post("http://192.168.1.11:8000", data , function(data, status){
            console.log("Data: " + data + "Status: " + status);
            });});});
            </script>"""
 
      strTable = strTable+f"</table>{page_script}</body></html>"
 
      with open("view_data.html", 'w', encoding="utf-8") as hs:
           hs.write(strTable)
 
