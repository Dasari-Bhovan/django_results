from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
import pymongo
def home(request):
    final_res=""
    context={"result":final_res}
    
    if request.method=="POST":
        
        client = pymongo.MongoClient("mongodb+srv://bhovan:mGxrijik1A8bga2i@results.oysj11d.mongodb.net/?retryWrites=true&w=majority")
        db = client["SampleResults"]
        Roll_no=str(request.POST.get("Rollno"))
        Reg="R"+Roll_no[:2]
        if "5A" in Roll_no:
            Reg="R"+str(int(Roll_no[:2])-1)

        # Get a reference to a collection
        # print("{Reg} Results")
        collection = db[f"{Reg} Results"]
        posts = collection.find({"_id":Roll_no})
        sem="2-1"
        
        for post in posts:
            res=dict(post)
        final_res=""
# print(res.items())
        print(res)
        for i in res.keys():
            if i=="_id" or i=="name":
                final_res+=i+":"+ res[i]+"<br>"
            elif i==sem:
                final_res+=sem+":\n"
                for j,k in res[i].items():
                    final_res+=j+" : "+k+"<br>"
        # print(final_res)
        context={'result':final_res}
        print(context)
    



    return render(request,"home.html",context=context)
