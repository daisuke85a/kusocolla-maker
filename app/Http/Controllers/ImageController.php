<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Image;

class ImageController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        \Log::info("post image");

        if ($request->file('image') != null) {
            // TODO: 本当に画像ファイルかどうか、のバリデーションを追加したい
            if ($request->file('image')->isValid()) {
                $image = \App\Models\Image::create(
                    ['name' => basename($request->image->store('public/image'))]
                );
                \Log::debug('アップロードした画像を保存しました');
            } else {
                \Log::debug('画像の保存に失敗しました');
            }
        } else {
            \Log::debug('画像が指定されていません');
        }

        return redirect("/image/{$image->id}");
    }

    /**
     * Display the specified resource.
     *
     * @param  Image $image
     * @return \Illuminate\Http\Response
     */
    public function show(Image $image)
    {
        return view('image', ['image' => $image->name]);
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  Image $image
     * @return \Illuminate\Http\Response
     */
    public function edit(Image $image)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  Image $image
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Image $image)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  Image $image
     * @return \Illuminate\Http\Response
     */
    public function destroy(Image $image)
    {
        //
    }
}
