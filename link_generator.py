
def generate_links(token:int,list_department:int,list_course:int)->list:
   link_list = []
   base_url = 'https://reports4u22.bgu.ac.il/GeneratePDF.php'
   for i in range(1,3):
      #itirate over the links
      for p_year in range(2020, 2024):
      # Construct the URL
            link_list.append(f'{base_url}?server=aristo4stu419c/report=SCRR016w/p_key={token}/p_year={p_year}/p_semester={i}/out_institution=0/grade=5/list_department=*{list_department}@/list_degree_level=*1@/list_course=*{list_course}@/LIST_GROUP=*@/P_FOR_STUDENT=1')
   return link_list
