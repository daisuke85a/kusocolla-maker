<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Image extends Model
{
    //
    protected $fillable = ['name','face_num'];

    public function getFolder() :string{
        return preg_replace('/\.[^.]+$/','',$this->name) . '_face'; 
    }

    public function getExtension() :string{
        return preg_replace('/^.*\.([^.]+)$/D', '$1', $this->name);
    }
}
