bootstrap
<!DOCTYPE html>
<html>
  <head>
    <title>Hello, World!</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
  <nav class = "navbar navbar-default">
    <ul class = "nav navbar-nav">
      <li class = "active"><a href = "#">Home</a></li>
      <li><a href = "#">pg1</a></li>
      <li><a href = "#">pg2</a></li>
    </ul>
  </nav>
    <div class = "glyphicon glyphicon-envelope"><!-- glyphicon-heart | glyphicon-print | glyphicon-search -->
      
    </div>
    <div class = "container-fluid headtop">
      <div class = "container headin">
        <div class = "row"> <!-- col-md-3 for laptop | col-sm-3 for tablet | col-xs-3 for mobile --> 
        <div class = "col-md-3"><
        <nav class = "navbar navbar-default">
          <button type = "button" class = "navbar-toggle" data-target = "menu" data-toggle = "collapse">
            <span class = "icon-bar"></span>
            <span class = "icon-bar"></span>
          </button>
          <div class = "collapse navbar-collapse" id = "menu">
          <ul class = "nav navbar-nav pagination">
            <li class = "active"><a href = "#">Home</a></li>
            <li><a href = "#">pg1</a></li>
            <li><a href = "#">pg2</a></li>
          </ul> </div>
          <ol class = "breadcrumb">
            <li class = "breadcrumb-item"><a href = "#">Home</a></li>
            <li class "breadcrumb-item active"><a href = "#">pg1</a></li>
            <li><a href = "#">pg2</a></li>
          </ol>
        </nav>
        </div>
          <div class = "col-md-3 bg-primary text-center text-capitalize"> <img src = ". jpg" width = "250" height = "250" class = "img-thmubnail"></div>
          <!--img-thumbnail | img-rounded | img-circle | img-responsive-->
          <!--div class = "col-md-3"></div-->
          <!-- pull-right | pull-left -->
          <div class = "col-md-6 col-xs-12 bg-danger text justify headin pull-right"> <p class = "text-warning"></p> </div>
          <div class = "col-md-3 bg-success"> Item3 </div>
          <div class = "col-md-12 bg-info text-center"> 
          <p class = "text-danger"> Item4 </p></div>
          <!-- text-left | text-center | text-right | text-justify | text-lowercase | text-uppercase | text-capitalize -->
          <!-- text-muted | text-primary | text-success | text-info | text-warning | text-danger -->
        </div>
      </div>
      <i class = "fab fa-twitter"></i>
    </div>
    <button type = "button" class = 'btn btn-primary'> <span class = 'glyphicon glyphicon-search'></span>Basic </button>
    <!-- btn btn-primary | btn btn-default | btn btn-success | btn btn-info | btn btn-warning | btn btn-danger | btn btn-link -->
    <!-- btn-lg | btn-sm | btn-xs -->
    <input type = "button" value = "Normal" name = "" class = "btn btn-primary btn-lg"/>
    <div class = "btn-group-vertical" > <!-- class = btn-group -->
      <button type = "button" class = "btn btn-primary"> Apple </button>
      <button type = "button" class = "btn btn-primary"> Mango </button>
      <button type = "button" class = "btn btn-primary"> Basic </button>
    </div>
    <div class = "col-md-8 tabledata visible-xs"><!-- visible-xs | visible-md| hidden-xs -->
      <div class = "table-responsive">
      <table class = "table table-striped"><!-- table table-bordered | table table-hover -->
        <thead></thead>
        <tbody>
          <tr class = "active"><!-- " danger" | "success" | "warning" -->
            
          </tr>
        </tbody>
      </table>
      </div>
    </div>
  </body>
</html>
<!-- breadcrumb-->
.container-fluid {
  padding-right : 15px;
  padding-left : 15px;
  margin-left : auto;
  margin-right : auto;
}
.headtop {
  background : lightgrey;
}
.headin {
  border : 1px solid red;
}
.tabledata{
  display : none;
