<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site" content="@daisuke7924" />
    <meta name="twitter:creator" content="@daisuke7924" />
    <meta property="og:url" content="{{url()->current()}}" />
    <meta property="og:title" content="クソコラメーカー" />
    <meta property="og:description" content="さぁみんなで、ごきげんになろう！" />
    <meta property="og:image" content="{{url("/")}}/storage/image/{{$image->getFolder()}}/add.{{$image->getExtension()}}" />
    <link href="{{ asset('css/app.css') }}" rel="stylesheet">
</head>
<body>
<a href="{{ url('/') }}">戻る</a>
@if ($image != null)
<p>合成した画像</p>
<div class="kusocolla">
  <div class="kusocolla__face face-01">
    @for($i =0; $i<$image->face_num; $i++)
        <img src="{{url("/")}}/storage/image/{{$image->getFolder()}}/{{$i}}.{{$image->getExtension()}}" alt="image" style="max-width:100%">
    @endfor
  </div>
  <div class="kusocolla__face face-02">
    @for($i =0; $i<$image->face_num; $i++)
        <img src="{{url("/")}}/storage/image/{{$image->getFolder()}}/{{$i}}.{{$image->getExtension()}}" alt="image" style="max-width:100%">
    @endfor
  </div>
  <div class="kusocolla__face face-03">
    @for($i =0; $i<$image->face_num; $i++)
        <img src="{{url("/")}}/storage/image/{{$image->getFolder()}}/{{$i}}.{{$image->getExtension()}}" alt="image" style="max-width:100%">
    @endfor
  </div>
</div>
<img src="{{url("/")}}/storage/image/{{$image->getFolder()}}/add.{{$image->getExtension()}}" alt="image" style="max-width:100%">
<p>顔だけ切り出した画像</p>
@for($i =0; $i<$image->face_num; $i++)
    <img src="{{url("/")}}/storage/image/{{$image->getFolder()}}/{{$i}}.{{$image->getExtension()}}" alt="image" style="max-width:100%">
@endfor
<div>
</div>
<p>アップロードした画像</p>
<img src="{{url("/")}}/storage/image/{{$image->name}}" alt="image" style="max-width:100%">
@endif
</body>
</html>