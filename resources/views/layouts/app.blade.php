<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title')</title>
    <link rel="stylesheet" href="/css/app.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css">
</head>

<body>
    <div class="siteheader">
        @include('inc.navbar')
    </div>
    <div class="welcomepage mt-5">
        @if (Request::is('/'))
            @include('inc.hero')
        @endif
    </div>
    <div class="sitecontent container mt-5">
        <div class="row">
            <div class="col-8">
                @yield('content')
            </div>
            <div class="col-4">
                @include('inc.aside')
            </div>
        </div>
    </div>
    <div class="sitefooter">
        @include('inc.footer')
    </div>
</body>

</html>
