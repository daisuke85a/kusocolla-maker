<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>お試し画面</title>

        <form action="image" method="post" enctype="multipart/form-data">
            {{ csrf_field() }}
            <div class="form-group @if($errors->has('image')) has-error @endif">
                <label for="image" class="col-md-3 control-label">画像ファイル</label>
                <div class="col-sm-9">
                    <input type="file" class="form-control" id="image" name="image">
                    @if($errors->has('image'))<span class=" text-danger">{{ $errors->first('image') }}</span>
                    @endif
                </div>
            </div>
            <div class="col-md-offset-3 text-center"><button class="btn btn-primary">アップロード</button></div>
        </form>
    </body>
</html>
