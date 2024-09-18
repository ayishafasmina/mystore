from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Products
from api.serializers import ProductSerializer,ProductModelSerializer,UserSerializer,CartSerializer

from rest_framework.viewsets import ViewSet,ModelViewSet

from rest_framework.decorators import action
from django.contrib.auth.models import User

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductView(APIView):

    def get(self,request,*args,**kw):

        qs=Products.objects.all()
        serializer=ProductSerializer(qs,many=True)

        return Response(data=serializer.data)
    
    def post(self,request,*args,**kw):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors) 
    

class ProductDetailView(APIView):
    def get(self,request,*args,**kw):
        print(kw)
        id=kw.get('id')
        qs=Products.objects.get(id=id)
        serializer=ProductSerializer(qs)
    
        return Response(data=serializer.data)
    


    def put(self,request,*args,**kw):
   
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            id=kw.get('id')
            Products.objects.filter(id=id).update(**request.data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors) 
    
    
    def delete(self,request,*args,**kw):
        id=kw.get('id')
        Products.objects.filter(id=id).delete()
        return Response(data='item successfully deleted')
    



# class ProductViewsetView(ViewSet):

#     def list(self,request,*args,**kw):

#         qs=Products.objects.all()
#         serializer=ProductModelSerializer(qs,many=True)
#         return Response(data=serializer.data)
    

#     def create(self,request,*args,**kw):
#         serializer=ProductModelSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
    
#     def retrieve(self,request,*args,**kw):
#         id=kw.get('pk')
#         qs=Products.objects.get(id=id)
#         serializer=ProductModelSerializer(qs)
    
#         return Response(data=serializer.data)
    
    
#     def destroy(self,request,*args,**kw):
#         id=kw.get('pk')
#         Products.objects.filter(id=id).delete()
#         return Response(data='item successfully deleted')

    
#     def update(self,request,*args,**kw):
#         id=kw.get('pk')
#         obj=Products.objects.get(id=id)
#         serializer=ProductModelSerializer(data=request.data,instance=obj)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
      
 
# #custom methods
# #@action -to return http methods 
#     @action(methods=['GET'],detail=False)       #detail=false get a periticular id  
    
#     def categories(self,request,*args,**kw):

#         qs=Products.objects.values_list('catogory',flat=True).distinct()       #get a unique value falt=true-to execute list format 

#         return Response(data=qs)
    


    

# class UserView(ViewSet):
#     def create(self,request,*args,**kw):
#         serializer=UserSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()



class ProductViewsetView(ModelViewSet):

    serializer_class=ProductModelSerializer
    queryset=Products.objects.all()

    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    @action(methods=['GET'],detail=False)
    def catogeries(self,request,*args,**kw):
       qs=Products.objects.values_list('catogory',flat=True).distinct()
       return Response(data=qs)
    

    @action(methods=["POST"],detail=True)
    def add_cart(self,request,*args,**kw):
        id=kw.get('pk')
        user=request.user                                            
        item=Products.objects.get(id=id)    
        user.carts_set.create(product=item) 

        return Response(data='item successfully added')
    
class CartView(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    def post(self,request,*args,**kw):
        id=kw.get('id')
        user=request.user                                            
        item=Products.objects.get(id=id)    
        user.carts_set.create(product=item) 

        return Response(data='item successfully added')
        
           
                          





    




