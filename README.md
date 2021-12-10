# CakeShop
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <style>
    /* Remove the navbar's default rounded borders and increase the bottom margin */ 
    .navbar {
      margin-bottom: 50px;
      border-radius: 0;
    }
    
    /* Remove the jumbotron's default bottom margin */ 
     .jumbotron {
      margin-bottom: 0;
    }
   
    /* Add a gray background color and some padding to the footer */
    footer {
      background-color: #f2f2f2;
      padding: 25px;
    }
  </style>
</head>
<body>

<div class="jumbotron">
  <div class="container text-center">
    <h1>Firstbit Cake Shop</h1>      
    <p>Tasty,Fresh and Delicious</p>
  </div>
</div>

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      {%if "uname" in request.session %}
      <a class="navbar-brand" href="#">Welcome {{request.session.uname}}</a>
      {%else%}
      <a class="navbar-brand" href="#">Logo</a>
      {%endif%}
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li class="active"><a href="/">Home</a></li>
        <li class="dropdown">
          <a class="dropdown-toggle" data-toggle="dropdown" href="#">Categories
          <span class="caret"></span></a>
          <ul class="dropdown-menu">
            {%for c in cats%}
            <li><a href="/ShowCakes/{{c.id}}">{{c.cname}}</a></li>
            {%endfor%}
            
          </ul>
        </li>
        <li><a href="#">Deals</a></li>
        <li><a href="#">Stores</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        {%if "uname" in request.session%}
        <li><a href="/Logout"><span class="glyphicon glyphicon-user"></span>Logout</a></li>        
        {%else%}
        <li><a href="/Login"><span class="glyphicon glyphicon-user"></span> Login</a></li>
        <li><a href="/SignUp"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
        {%endif%}
        
        <li><a href="/ShowAllCartItems"><span class="glyphicon glyphicon-shopping-cart"></span> Cart</a></li>
      </ul>
    </div>
  </div>
</nav>



<div class="container">  
  <div class="row">    
    {%for cake in cakes%}
    <div class="col-sm-4">      
      <div class="panel panel-primary">
        <div class="panel-heading">{{cake.cakename}}</div>
        <div class="panel-body"><img src="{{cake.imageUrl.url}}" class="img-responsive" style="width:120px;height:140px" alt="Image"></div>
        <div class="panel-footer">Description: {{cake.description}}</div>
        <div class="panel-footer">Price : {{cake.price}} 
          <p><a href="/ViewDetails/{{cake.id}}">View Details</a></p></div>
      </div>      
    </div>
    {%endfor%}  
  </div>
  
</div><br>

{%endblock%}
<footer class="container-fluid text-center">
  <p>Online Store Copyright</p>  
  <form class="form-inline">Get deals:
    <input type="email" class="form-control" size="50" placeholder="Email Address">
    <button type="button" class="btn btn-danger">Sign Up</button>
  </form>
</footer>

</body>
</html>
