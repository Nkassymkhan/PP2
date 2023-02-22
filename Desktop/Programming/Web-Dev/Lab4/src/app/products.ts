export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  url: string;
}

export const products = [
  {
    id: 1,
    name: 'Смарт-часы Apple Watch Series 8 45 мм Aluminum черный',
    price: 500,
    description: "Поддержка платформ: iOS, Материал корпуса: алюминий, Цвет корпуса: черный, Объем встроенной памяти: 32 Гб ",
    url: 'https://kaspi.kz/shop/p/apple-watch-series-8-45-mm-aluminum-chernyi-106362847/?c=750000000#!/item',
    photo: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h1a/h69/63158968057886/apple-watch-series-8-41-mm-cernyj-106362847-1.jpg',
    rating:'✰✰✰✰✰',
  },
  {
    id: 2,
    name: 'Смарт-часы Apple Watch SE 2nd Gen 40 мм золотистый',
    price: 459,
    description: 'Поддержка платформ: iOS, Материал корпуса: алюминий, Цвет корпуса: золотистый, Объем встроенной памяти: 32 Гб',
    url: 'https://kaspi.kz/shop/p/apple-watch-se-2nd-gen-40-mm-zolotistyi-106362759/?c=750000000#!/item',
    rating:'✰✰✰✰✰',
    photo: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h97/h46/62711073407006/apple-watch-se-2nd-generation-40-mm-zolotistyj-106362759-1.jpg'
  },
  {
    id: 3,
    name: 'Samsung Galaxy Watch 4 Classic SM-R890NZKACIS 46 мм',
    price: 95.9,
    description: 'Поддержка платформ: Android, Материал корпуса: алюминий, Цвет корпуса: черный, Интерфейсы: Bluetooth, ,NFC',
    url: 'https://kaspi.kz/shop/p/samsung-galaxy-watch-4-classic-sm-r890nzkacis-46-mm-chernyi-chernyi-102170938/?c=750000000#!/item',
    rating:'✰✰✰✰',
    photo:'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h6c/h85/62047597592606/samsung-galaxy-watch-4-classic-sm-r890-cernyj-102170938-1-Container.jpg'
  },
  {
    id: 4,
    name: 'Apple Watch Series 8 41 мм Aluminum золотистый',
    price: 519,
    description: 'Поддержка платформ: iOS, Материал корпуса: алюминий, Цвет корпуса: starlight',
    url: 'https://kaspi.kz/shop/p/apple-watch-series-8-41-mm-aluminum-zolotistyi-106585035/?c=750000000#!/item',
    rating:'✰✰✰✰✰',
    photo:'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h60/hfa/63158666461214/apple-watch-series-8-41-mm-aluminum-zolotistyj-106585035-1.jpg'

  },
  {
    id: 5,
    name: 'Xiaomi Redmi Watch 2 Lite GL черный',
    price: 99,
    description: 'Поддержка платформ: iOS, Android, Материал корпуса: пластик, Цвет корпуса: черный',
    url: 'https://kaspi.kz/shop/p/xiaomi-redmi-watch-2-lite-gl-chernyi-103246651/?c=750000000#!/item',
    rating:'✰✰✰',
    photo:'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/he4/hdc/47874442559518/smart-casy-xiaomi-redmi-watch-2-lite-gl-black-103246651-1.jpg'
  },
  {
    id: 6,
    name: 'Смарт-часы Apple Watch SE 44 мм серый',
    price: 399,
    description: 'Поддержка платформ: iOS, Материал корпуса: алюминий, Цвет корпуса: серый',
    url: 'https://kaspi.kz/shop/p/apple-watch-se-44-mm-seryi-100568195/?c=750000000#!/item',
    rating:'✰✰✰✰',
    photo:'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hcd/he9/46637897416734/apple-watch-se-44mm-space-gray-aluminium-case-with-sport-band-mydt2gk-a-cernyj-100568195-1-Container.jpg'
  },
  {
    id: 7,
    name: 'Смарт-часы Aimoto Element розовый',
    price: 19,
    description: 'Поддержка платформ: iOS, Android, Материал корпуса: пластик, Цвет корпуса: розовый',
    url: 'https://kaspi.kz/shop/p/aimoto-element-rozovyi-100828444/?c=750000000#!/item',
    rating:'✰',
    photo: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hc8/h5e/33034415833118/aimoto-element-pink-100828444-1-Container.jpg'
  },
  {
    id: 8,
    name: 'COLMI P28 Plus черный',
    price: 45.9,
    description: 'Поддержка платформ: iOS, Android, Материал корпуса: пластик, Цвет корпуса: черный',
    url: 'https://kaspi.kz/shop/p/colmi-p28-plus-chernyi-106096505/?c=750000000#!/item',
    rating:'✰✰✰',
    photo: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hbb/he5/61766572539934/colmi-p28-plus-chernyi-106096505-1.jpg'
  },
  {
    id: 9,
    name: 'Смарт-часы Kieslect L11 золотистый',
    price: 50.9,
    description: 'Поддержка платформ: iOS, Android, Материал корпуса: алюминий, Цвет корпуса: золотистый',
    url: 'https://kaspi.kz/shop/p/kieslect-l11-zolotistyi-104688717/?c=750000000#!/item',
    rating:'✰✰✰✰',
    photo: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hc4/hc4/50421686206494/xiaomi-kieslect-l11-zolotistyj-zolotistyj-104688717-1.jpg'
  },
  {
    id: 10,
    name: 'Смарт-часы Smart Baby Watch Z6 GPS зеленый',
    price: 20,
    description: 'Поддержка платформ: iOS, Android, Материал корпуса: пластик, Цвет корпуса: черный',
    url: 'https://kaspi.kz/shop/p/smart-baby-watch-z6-gps-zelenyi-101910569/?c=750000000#!/item',
    rating:'✰✰',
    photo: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/haa/h6f/62047531434014/smart-baby-watch-z6-gps-zelenyj-101910569-1-Container.jpg'
  }

];


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/