@if ($image != null)
<p>顔だけ切り出した画像</p>
@for($i =0; $i<$image->face_num; $i++)
    <img src="/storage/image/{{$image->getFolder()}}/{{$i}}.{{$image->getExtension()}}" alt="image" style="max-width:100%">
@endfor
<div>
<a href="{{ url('/') }}">戻る</a>
</div>
<p>アップロードした画像</p>
<img src="/storage/image/{{$image->name}}" alt="image" style="max-width:100%">
@endif
