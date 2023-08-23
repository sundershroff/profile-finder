from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from chat.models import *
from profile_finder.models  import *

#@login_required
def messages_page(request):
    profile_finder_email=request.session['email']
    print("Email : "+profile_finder_email)
    pfdata = profile_finder.objects.filter(email=profile_finder_email).values()
    pfdata_id = pfdata[0]['id']
    print(pfdata_id)
    profil_image = pfdata[0]['profile_picture']
    thread = Thread.objects.by_user(user=pfdata_id).prefetch_related('chatmessage_thread').order_by('timestamp')
    # threads = Thread.objects.get()
    # context = {
    #     'Threads': threads
    # }
    
    #threads = Thread.objects.filter(first_person=pfdata_id).values()
    threads = Thread.objects.filter(Q(first_person=pfdata_id) | Q(second_person=pfdata_id)).values()
    print(threads)
    #print(len(threads))
    pfdatasarrname = []
    pfdatasarrimage = []
    pfdatasarrid = []
    pfmessageto = []
    messages = []
    for x in range(len(threads)):
        #print(threads[x])
        sid = threads[x]['first_person']
        rid = threads[x]['second_person']
        sidint = int(sid)
        ridint = int(rid)
        tid = threads[x]['id']
        pfdatasarrid.append(tid)
        print(sid)
        print(rid)
        if(pfdata_id == sidint):
            print("Same")
        else:
            pfdatas = profile_finder.objects.filter(id=sidint).values()
            if(pfdatas[0]['profileforwho'] == "myself"):
                name = pfdatas[0]['name']
            else:
                name = pfdatas[0]['nameo']
            image = pfdatas[0]['profile_picture']

            pfdatasarrname.append(name)
            pfdatasarrimage.append(image)
            pid = pfdatas[0]['id']
            pfmessageto.append(pid)
            print("NOT FIRST")
        if(pfdata_id == ridint):
            print("Same")
        else:
            pfdatas = profile_finder.objects.filter(id=ridint).values()
            if(pfdatas[0]['profileforwho'] == "myself"):
                name = pfdatas[0]['name']
            else:
                name = pfdatas[0]['nameo']
            image = pfdatas[0]['profile_picture']
            pfdatasarrname.append(name)
            pfdatasarrimage.append(image)
            pid = pfdatas[0]['id']
            pfmessageto.append(pid)
            print("NOT SECOND")


    
    # threads1 = Thread.objects.filter(second_person=pfdata_id).values()
    # print(len(threads1))
    
    # for x in range(len(threads1)):
    #     #print(threads[x])
    #     sid = threads1[x]['first_person']
    #     rid = threads1[x]['second_person']
    #     sidint = int(sid)
    #     ridint = int(rid)
    #     print(sid)
    #     print(rid)
    #     if(pfdata_id == sidint):
    #         print("Same")
    #     else:
    #         pfdatas = profile_finder.objects.filter(id=sidint).values()
    #         if(pfdatas[0]['profileforwho'] == "myself"):
    #             name = pfdatas[0]['name']
    #         else:
    #             name = pfdatas[0]['nameo']
    #         image = pfdatas[0]['profile_picture']
    #         pfdatasarrname.append(name)
    #         pfdatasarrimage.append(image)
   
    #     if(pfdata_id == ridint):
    #         print("Same")
    #     else:
    #         pfdatas = profile_finder.objects.filter(id=ridint).values()
    #         if(pfdatas[0]['profileforwho'] == "myself"):
    #             name = pfdatas[0]['name']
    #         else:
    #             name = pfdatas[0]['nameo']
    #         image = pfdatas[0]['profile_picture']
    #         pfdatasarrname.append(name)
    #         pfdatasarrimage.append(image)
    print(pfdatasarrname)
    print(pfdatasarrimage)
    datas = zip(pfdatasarrname,pfdatasarrimage,pfdatasarrid) 
    da = zip(pfdatasarrname,pfdatasarrimage,pfdatasarrid,pfmessageto) 


    for i in range(len(pfdatasarrid)):
        mes = ChatMessage.objects.filter(thread=pfdatasarrid[i]).values()
        messages.append(mes)
    print(messages)

    return render(request, 'messages.html',{'datas':datas,'pfdata_id':pfdata_id,"da":da,"thread":thread,"message":messages,"profil_image":profil_image})
