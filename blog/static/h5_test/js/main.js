(function () {
  'use strict';

  var modalMessage = {
    "id": 1162,
    platform: "web",
    "contentMetadata": {
      style: {
        width: '388px'
      },
      config: {
        position: 'center'
      },
      components: [{
        type: 'img',
        config: {
          "src": "https://statics.growingio.com/media/20190529/3/1559099193082/0529img.png",
          target: {}
        },
        style: {
          'max-width': '388px',
          'margin': '0 auto',
          'display': 'block'
        }
      }, {
        type: 'caption',
        style: {
          'text-align': 'center',
          'word-wrap': 'break-word',
          'padding': '0 10px',
          'margin': '10px 0'
        },
        config: {
          text: '你看我呀'
        }
      }, {
        type: 'paragraph',
        style: {
          'padding': '0 10px',
          'text-align': 'center',
          'margin': '10px 0'
        },
        config: {
          "text": "点我copy，你有本事就点点点我copy，你有本事就点点点我copy，你有本事就点点点我copy，你有本事就点点点我copy，你有本事就点点点我copy，你有本事就点点点我copy，你有本事就点点"
        }
      }, {
        type: 'button',
        style: {
          margin: '10px auto 10px',
          width: '160px',
          height: '43px'
        },
        "config": {
          "text": "点击我Copy",
          "target": {
            "copy": "你好呀"
          }
        }
      }]
    },
    "updateAt": 1559216893880,
    "rule": {
      "type": "system",
      "action": "pageOpen",
      "endAt": 4102416000000,
      "startAt": 946656000000,
      "triggerPages": ["test.growingio.com:10001"],
      "triggerCd": 300,
      "triggerDelay": 5,
      "limit": 1
    },
    "env": {
      "isDebugMode": true
    }
  };

  var modalMessage$1 = {
    "id": 1163,
    platform: "web",
    "contentMetadata": {
      style: {
        width: '388px'
      },
      config: {
        position: 'center'
      },
      components: [{
        type: 'img',
        config: {
          "src": "https://statics.growingio.com/media/20190529/3/1559099193082/0529img.png",
          target: {}
        },
        style: {
          'max-width': '388px',
          'margin': '0 auto',
          'display': 'block'
        }
      }, {
        type: 'caption',
        style: {
          'text-align': 'center',
          'word-wrap': 'break-word',
          'padding': '0 10px',
          'margin': '10px 0'
        },
        config: {
          text: '你看我呀'
        }
      }, {
        type: 'paragraph',
        style: {
          'padding': '0 10px',
          'text-align': 'center',
          'margin': '10px 0'
        },
        config: {
          "text": "点我跳转，有本事你就点点"
        }
      }, {
        type: 'button',
        style: {
          margin: '10px auto 10px',
          width: '160px',
          height: '43px'
        },
        "config": {
          "text": "点我跳转",
          "target": {
            "href": "http://www.baidu.com"
          }
        }
      }]
    },
    "updateAt": 1559216893880,
    "rule": {
      "type": "system",
      "action": "pageOpen",
      "endAt": 4102416000000,
      "startAt": 946656000000,
      "triggerPages": ["test.growingio.com:10001"],
      "triggerCd": 300,
      "triggerDelay": 5,
      "limit": 1
    },
    "env": {
      "isDebugMode": true
    }
  };

  var modalMessage$2 = {
    "id": 1164,
    platform: "web",
    "contentMetadata": {
      style: {
        width: '388px'
      },
      config: {
        position: 'center'
      },
      components: [{
        type: 'img',
        config: {
          "src": "https://statics.growingio.com/media/20190529/3/1559099193082/0529img.png",
          target: {}
        },
        style: {
          'max-width': '388px',
          'margin': '0 auto',
          'display': 'block'
        }
      }, {
        type: 'caption',
        style: {
          'text-align': 'center',
          'word-wrap': 'break-word',
          'padding': '0 10px',
          'margin': '10px 0'
        },
        config: {
          text: '你看我呀'
        }
      }, {
        type: 'paragraph',
        style: {
          'padding': '0 10px',
          'text-align': 'center',
          'margin': '10px 0'
        },
        config: {
          "text": "点我关闭，有本事你就点点"
        }
      }, {
        type: 'button',
        style: {
          margin: '10px auto 10px',
          width: '160px',
          height: '43px'
        },
        "config": {
          "text": "点击我关闭",
          "target": {}
        }
      }]
    },
    "updateAt": 1559216893880,
    "rule": {
      "type": "system",
      "action": "pageOpen",
      "endAt": 4102416000000,
      "startAt": 946656000000,
      "triggerPages": ["test.growingio.com:10001"],
      "triggerCd": 300,
      "triggerDelay": 5,
      "limit": 1
    },
    "env": {
      "isDebugMode": true
    }
  };

  var h5 = {
    "id": 1162,
    platform: "h5",
    "contentMetadata": {
      id: "123,",
      type: 'modal',
      config: {
        position: 'center',
        closeable: false
      },
      style: {
        'width': '80vw'
      },
      components: [{
        type: 'img',
        style: {
          width: "100%"
        },
        config: {
          src: 'https://statics.growingio.com/media/20190529/3/1559099193082/0529img.png',
          ctd: true,
          target: {}
        }
      }, {
        type: 'icon',
        style: {
          width: '5vw',
          height: '5vw',
          margin: '3vw auto 0',
          display: 'block'
        },
        config: {
          name: 'VClose',
          closeable: true
        }
      }]
    },
    "updateAt": 1559216893880,
    "rule": {
      "type": "system",
      "action": "pageOpen",
      "endAt": 4102416000000,
      "startAt": 946656000000,
      "triggerPages": ["test.growingio.com:10001"],
      "triggerCd": 300,
      "triggerDelay": 5,
      "limit": 1
    },
    "env": {
      "isDebugMode": true
    }
  };

  var popups = {
    popup_1: modalMessage,
    popup_2: modalMessage$1,
    popup_3: modalMessage$2,
    h5: h5
  };

  /*! *****************************************************************************
  Copyright (c) Microsoft Corporation. All rights reserved.
  Licensed under the Apache License, Version 2.0 (the "License"); you may not use
  this file except in compliance with the License. You may obtain a copy of the
  License at http://www.apache.org/licenses/LICENSE-2.0

  THIS CODE IS PROVIDED ON AN *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED
  WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR PURPOSE,
  MERCHANTABLITY OR NON-INFRINGEMENT.

  See the Apache Version 2.0 License for specific language governing permissions
  and limitations under the License.
  ***************************************************************************** */

  var __assign = function() {
      __assign = Object.assign || function __assign(t) {
          for (var s, i = 1, n = arguments.length; i < n; i++) {
              s = arguments[i];
              for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p)) t[p] = s[p];
          }
          return t;
      };
      return __assign.apply(this, arguments);
  };

  function traverse(collection, fn) {
    var index = 0;

    for (; index < collection.length; index++) {
      fn(collection[index], index);
    }
  }

  function reduce(callback, collection, initialValue) {
    var _initialValue = initialValue;
    traverse(collection, function (value, index) {
      if (_initialValue === undefined) {
        _initialValue = value;
      } else {
        _initialValue = callback(_initialValue, value, index);
      }
    });
    return _initialValue;
  }

  function map(collection, fn) {
    var values = [];
    traverse(collection, function (v, i) {
      return values.push(fn(v, i));
    });
    return values;
  }

  function filter(collection, fn) {
    var values = [];
    traverse(collection, function (v, i) {
      if (fn(v, i)) values.push(v);
    });
    return values;
  }

  function foreach(collection, fn) {
    if (collection.constructor == Array) {
      traverse(collection, fn);
    } else {
      for (var key in collection) {
        if (Object.hasOwnProperty.call(collection, key)) {
          fn(collection[key], key);
        }
      }
    }
  }

  var removeNode = function removeNode(node) {
    if (!!node.remove) {
      node.remove();
    } else if (node.parentNode) {
      node.parentNode.removeChild(node);
    }
  };

  function addEventListener(elem, type, listener, useCapture) {
    if (useCapture === void 0) {
      useCapture = false;
    }

    if (elem.addEventListener) {
      elem.addEventListener(type, listener, useCapture);
    } else if (elem.attachEvent) {
      elem.attachEvent("on" + type, listener);
    } else {
      elem["on" + type] = listener;
    }
  }

  function isFunction(obj) {
    return typeof obj === 'function';
  }
  function isString(obj) {
    return typeof obj === 'string';
  }
  function isNil(obj) {
    return typeof obj === 'undefined' || obj === null;
  }

  var Pending = 0;
  var Fulfilled = 1;
  var Rejected = 2;

  var Future = function () {
    function Future(executor) {
      var _this = this;

      this.$state = Pending;
      this.$chained = [];

      var resolve = function resolve(value) {
        if (_this.$state !== Pending) {
          return;
        }

        _this.$state = Fulfilled;
        _this.$internalValue = value;
        foreach(_this.$chained, function (_) {
          return _.onFulfilled && _.onFulfilled(value);
        });
        return;
      };

      var reject = function reject(err) {
        if (_this.$state !== Pending) {
          return;
        }

        setTimeout(function () {
          _this.$state = Rejected;
          _this.$internalValue = err;

          if (filter(_this.$chained, function (_) {
            return !!_.onRejected;
          }).length === 0) {
            if (!Future.handleUnResolveError) {
              console.log(JSON.stringify(err));
              console.log('Unprocessed Future Exception.');
            } else {
              Future.handleUnResolveError(err);
            }
          }

          foreach(_this.$chained, function (_) {
            return _.onRejected && _.onRejected(err);
          });
        }, 0);
        return;
      };

      try {
        executor(resolve, reject);
      } catch (err) {
        reject(err);
      }
    }

    Future.prototype.map = function (fn) {
      return this.flatMap(function (v) {
        return Future.successful(fn(v));
      });
    };

    Future.prototype.then = function (fn) {
      return this.map(fn);
    };

    Future.prototype.flatMap = function (fn) {
      var _this = this;

      return new Future(function (resolve, reject) {
        _this.onComplete(function (v) {
          try {
            fn(v).onComplete(resolve, reject);
          } catch (e) {
            reject(e);
          }
        }, reject);
      });
    };

    Future.prototype.foreach = function (fn) {
      this.map(function (value) {
        return fn(value);
      });
    };

    Future.prototype.failWith = function (onRejected) {
      this.onComplete(function (_) {
        return _;
      }, onRejected);
    };

    Future.prototype.recoverWith = function (fn) {
      var _this = this;

      return new Future(function (resolve, reject) {
        _this.failWith(function (reason) {
          try {
            resolve(fn(reason));
          } catch (e) {
            reject(e);
          }
        });
      });
    };

    Future.prototype.recover = function (fn) {
      return this.recoverWith(fn).flatMap(function (_) {
        return _;
      });
    };

    Future.prototype.onComplete = function (resolve, reject) {
      if (this.$state === Fulfilled) {
        resolve(this.$internalValue);
      } else if (this.$state === Rejected) {
        reject(this.$internalValue);
      } else {
        this.$chained.push({
          onFulfilled: resolve,
          onRejected: reject
        });
      }
    };

    Future.prototype.eventually = function (fn) {
      this.map(function (_) {
        return fn();
      }).recoverWith(function (error) {
        fn();
        throw error;
      });
    };

    Future.successful = function (value) {
      return new Future(function (resolve) {
        if (isFunction(value)) {
          resolve(value());
        } else {
          resolve(value);
        }
      });
    };

    Future.failed = function (reason) {
      return new Future(function (_, reject) {
        return reject(reason);
      });
    };

    Future.sequence = function (jobs) {
      return reduce(function (prev, next) {
        return prev.flatMap(function (prevValue) {
          return next.map(function (curValue) {
            return prevValue.concat(curValue);
          });
        });
      }, jobs, Future.successful([]));
    };

    return Future;
  }();

  function object(o) {
    var F = function () {
      function F() {}

      return F;
    }();

    F.prototype = o;
    return new F();
  }

  function Extend(SuperType, SubType) {
    var prototype = object(SuperType.prototype);
    var subPrototype = SubType.prototype;
    prototype.constructor = SubType;
    foreach(subPrototype, function (_, k) {
      prototype[k] = subPrototype[k];
    });
    SubType.prototype = prototype;
  }

  var HttpError = function () {
    function HttpError(message, code) {
      if (code === void 0) {
        code = 499;
      }

      Error.call(this, message);
      this.name = 'HttpError';
      this.code = code;
    }

    return HttpError;
  }();

  Extend(Error, HttpError);

  var cssPrefixes = ["Webkit", "Moz", "ms"],
      emptyStyle = document.createElement("div").style,
      vendorProps = {};

  function vendorPropName(name) {
    var capName = name[0].toUpperCase() + name.slice(1),
        i = cssPrefixes.length;

    while (i--) {
      name = cssPrefixes[i] + capName;

      if (name in emptyStyle) {
        return name;
      }
    }
  }

  function finalPropName(name) {
    var final = vendorProps[name];

    if (final) {
      return final;
    }

    if (name in emptyStyle) {
      return name;
    }

    return vendorProps[name] = vendorPropName(name) || name;
  }

  var rmsPrefix = /^-ms-/;
  var rdashAlpha = /-([a-z])/g;

  function camelCase(str) {
    return str.replace(rdashAlpha, function (_all, letter) {
      return letter.toUpperCase();
    });
  }

  function cssCamelCase(str) {
    return camelCase(str.replace(rmsPrefix, "ms-"));
  }

  function css(elem, styles) {
    foreach(styles, function (style, name) {
      name = cssCamelCase(name);
      name = finalPropName(name);

      try {
        elem.style[name] = style;
      } catch (e) {}
    });
    elem.style['boxSizing'] = 'border-box';
  }

  function createComponent(type, props, children) {
    var current = document.createElement(type);
    props.innerHtml && (current.innerHTML = props.innerHtml);
    props.id && (current.id = props.id);
    props.className && (current.className = props.className);
    props.style && css(current, props.style);
    props.onClick && addEventListener(current, 'click', function (e) {
      return props.onClick(e, current);
    });

    function wrapperText(str) {
      return document.createTextNode(str);
    }

    function render(node) {
      if (Object.prototype.toString.call(node) !== '[object Array]') {
        node = [node];
      }

      foreach(node, function (node) {
        if (isString(node)) {
          current.appendChild(wrapperText(node));
        } else if (isFunction(node)) {
          render(node());
        } else {
          current.appendChild(node);
        }
      });
    }

    if (children) {
      render(children);
    }

    return current;
  }
  var img = function img(props) {
    var img = createComponent('img', props);
    props.onLoad && addEventListener(img, 'load', function (e) {
      return props.onLoad(e, img);
    });
    props.onError && addEventListener(img, 'error', function (e) {
      return props.onError(e);
    });
    img.src = props.src;
    return img;
  };
  var div = function div(props, children) {
    return createComponent('div', props, children);
  };
  var svg = function svg(props) {
    var current = div({
      innerHtml: props.innerHtml
    }).firstElementChild;
    props.id && (current.id = props.id);
    props.style && css(current, props.style);
    props.onClick && addEventListener(current, 'click', function (e) {
      return props.onClick(e);
    });
    return current;
  };
  var i = function i(props) {
    return createComponent('i', props);
  };

  var Option = function () {
    function Option() {}

    Option.prototype.isDefined = function () {
      return !this.isEmpty();
    };

    Option.build = function (v) {
      return isNil(v) ? None : Some(v);
    };

    Option.nonEmptyString = function (str) {
      return Option.build(str).filter(function (_) {
        return isString(_) && _.length > 0;
      });
    };

    return Option;
  }();

  var INone = function () {
    function INone() {}

    INone.prototype.isEmpty = function () {
      return true;
    };

    INone.prototype.isDefined = function () {
      return false;
    };

    INone.prototype.map = function (f) {
      return None;
    };

    INone.prototype.foreach = function (_) {};

    INone.prototype.flatMap = function (_) {
      return None;
    };

    INone.prototype.filter = function (_) {
      return None;
    };

    INone.prototype.orFillWith = function (fn) {
      return fn();
    };

    INone.prototype.getOrElse = function (a) {
      return a;
    };

    INone.prototype.get = function () {
      throw new Error('NoSuchElementException');
    };

    INone.prototype.getOrElseL = function (f) {
      return f();
    };

    INone.prototype.toString = function () {
      return undefined;
    };

    return INone;
  }();

  var ISome = function () {
    function ISome(value) {
      this.value = value;
    }

    ISome.prototype.isEmpty = function () {
      return false;
    };

    ISome.prototype.isDefined = function () {
      return true;
    };

    ISome.prototype.map = function (f) {
      return Some(f(this.value));
    };

    ISome.prototype.foreach = function (f) {
      return f(this.value);
    };

    ISome.prototype.flatMap = function (f) {
      return f(this.value);
    };

    ISome.prototype.filter = function (f) {
      if (f(this.value)) return Some(this.value);else return None;
    };

    ISome.prototype.orFillWith = function (_) {
      return this;
    };

    ISome.prototype.getOrElse = function (a) {
      return this.value;
    };

    ISome.prototype.getOrElseL = function (_) {
      return this.value;
    };

    ISome.prototype.get = function () {
      return this.value;
    };

    ISome.prototype.toString = function () {
      return this.value.toString();
    };

    return ISome;
  }();

  Extend(Option, ISome);
  Extend(Option, INone);
  var None = new INone();
  function Some(v) {
    return new ISome(v);
  }

  function getParameterByName(name, url) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
  }

  var NameSpace = 'gio_plugin_gtouch';
  var protocol = 'https:' == document.location.protocol ? 'https://' : 'http://';
  var injectorTag = document.currentScript && document.getElementById(NameSpace + "-inject");
  var __USING_SCRIPT_INJECT__ = !!injectorTag && injectorTag['$onload'];
  var IconHost = !!injectorTag ? function () {
    var injectorTagSrc = injectorTag.src.split('/');
    injectorTagSrc[injectorTagSrc.length - 1] = 'icons.png';
    return injectorTagSrc.join('/');
  }() : '';
  var isDebugMode = !!getParameterByName('growingio-sdk-test', window.location.href);
  var inPhone = function () {
    var sUserAgent = navigator.userAgent.toLowerCase();

    var indexOf = function indexOf(platform) {
      return sUserAgent.indexOf(platform);
    };

    var bIsIpad = indexOf('ipad') > -1;
    var bIsIphoneOs = indexOf('iphone os') > -1;
    var bIsMidp = indexOf('midp') > -1;
    var bIsUc7 = indexOf('rv:1.2.3.4') > -1;
    var bIsUc = indexOf('ucweb') > -1;
    var bIsAndroid = indexOf('android') > -1;
    var bIsCE = indexOf('windows ce') > -1;
    var bIsWM = indexOf('windows mobile') > -1;
    return bIsIpad || bIsIphoneOs || bIsMidp || bIsUc7 || bIsUc || bIsAndroid || bIsCE || bIsWM;
  }();

  function createIcon(name, props) {
    var _style = {
      'background': "url(" + IconHost + ")",
      'background-repeat': 'no-repeat',
      'vertical-align': 'middle',
      'display': 'inline-block'
    };
    return function () {
      return i(__assign({}, props, {
        style: __assign({}, _style, props.style),
        className: "_gio_c_icon _gio_c_icon_" + name
      }));
    };
  }

  var BuiltInIcons = {
    Check: function Check(props) {
      if (props === void 0) {
        props = {};
      }

      return createIcon('check', __assign({}, props, {
        style: __assign({
          'background-position': '-12px -12px',
          'width': '16px',
          'height': '16px'
        }, props.style)
      }));
    },
    Close: function Close(props) {
      if (props === void 0) {
        props = {};
      }

      return createIcon('close', __assign({}, props, {
        style: __assign({
          'background-position': '-128px -8px',
          'width': '24px',
          'height': '24px'
        }, props.style)
      }));
    },
    VClose: function VClose(props) {
      return function () {
        return svg(__assign({}, props, {
          innerHtml: "<svg viewBox=\"0 0 1080 1024\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" width=\"25\" height=\"25\">\n      <path d=\"M1003.064889 9.159111l40.220444 40.220445-965.404444 965.404444-40.277333-40.163556z\" fill=\"#D0D0D0\"></path>\n      <path d=\"M1043.285333 974.620444l-40.220444 40.220445L37.660444 49.436444 77.767111 9.102222z\" fill=\"#D0D0D0\"></path>\n      </svg>"
        }));
      };
    }
  };

  function ModalConfigBuilder(config) {
    if (config === void 0) {
      config = {};
    }

    return {
      position: Option.build(config.position).getOrElse('center')
    };
  }

  function iEShaodw(color, direction, strength) {
    return "progid:DXImageTransform.Microsoft.Shadow(color=" + color + " direction=" + direction + ", strength=" + strength + ")";
  }

  var modalStyle = {
    'display': 'inline-block',
    'overflow': 'hidden',
    'position': 'relative',
    'background': '#fff',
    'border-radius': '3px',
    'z-index': 2147483646,
    'box-shadow': '0 4px 6px 0 rgba(112,112,112,0.5)',
    '-moz-box-shadow': '0 4px 6px 0 rgba(112,112,112,0.5)',
    '-webkit-box-shadow': '0 4px 6px 0 rgba(112,112,112,0.5)',
    'zoom': 1,
    'filter': iEShaodw('#707070', 0, 1) + " " + iEShaodw('#707070', 90, 3) + " " + iEShaodw('#707070', 180, 3) + " " + iEShaodw('#707070', 270, 1)
  };
  function Modal(style, config, handlers) {
    if (config === void 0) {
      config = {};
    }

    return Future.successful(function () {
      config = ModalConfigBuilder(config);
      var modal = div({
        className: "_gio_c_modal _gio_c_modal_" + config.position,
        style: __assign({}, modalStyle, style)
      }, div({
        className: '_gio_c_modal__close',
        onClick: handlers && handlers.closeWindowAndTrack,
        style: {
          'z-index': 2147483647,
          'top': '10px',
          'right': '10px',
          'position': 'absolute',
          'cursor': 'pointer'
        }
      }, BuiltInIcons.Close()));
      return Option.build(modal);
    });
  }

  var transform = function transform(_) {
    var result = _.map(function (_) {
      return _.map(function (v) {
        return Option.build(v);
      });
    }).getOrElse(Future.successful(None));

    return result;
  };

  var TemplateBuilder = function () {
    function TemplateBuilder(message) {
      this.message = message;
      this.id = message.id.toString();
      this.position = ModalConfigBuilder(message.contentMetadata.config).position;
    }

    TemplateBuilder.prototype.className = function () {
      return "gio-modal-anchor-" + this.position;
    };

    TemplateBuilder.prototype.renderComponent = function (rootComponent, handlers) {
      var _this = this;

      var data = this.component2Html(rootComponent, handlers).map(function (componentOpt) {
        return componentOpt.flatMap(function (renderedComponent) {
          return Option.build(rootComponent.components).map(function (childComponents) {
            var traverseRenderComponents = function traverseRenderComponents() {
              return map(childComponents, function (rawComponent) {
                return _this.component2Html(rawComponent, handlers);
              });
            };

            return Future.sequence(traverseRenderComponents()).map(function (components) {
              return reduce(function (parent, child) {
                child.foreach(function (_) {
                  return parent.appendChild(_);
                });
                return parent;
              }, components, renderedComponent);
            });
          });
        });
      }).flatMap(function (_) {
        return transform(_);
      });
      return data;
    };

    return TemplateBuilder;
  }();

  var paragraphStyle = {
    'font-size': '12px',
    'white-space': 'pre-wrap',
    'word-break': 'break-word'
  };
  function Paragraph(style, config) {
    return Future.successful(function () {
      return Option.nonEmptyString(config.text).map(function (text) {
        return div({
          className: "_gio_c_paragraph",
          style: __assign({}, paragraphStyle, style)
        }, text);
      });
    });
  }

  function redirectOnClick(href, callback) {
    return function (e, current) {
      callback && callback();

      if (window.open && !inPhone) {
        window.open(href);
      } else {
        window.location.href = href;
      }
    };
  }

  var buttonStyle = {
    'font-size': '14px',
    'max-height': '100px',
    'font-weight': '500',
    'cursor': 'pointer',
    'display': 'block',
    'background-image': 'none',
    'border': '1px solid transparent',
    'white-space': 'nowrap',
    'line-height': '1.5',
    'padding': '4px 15px',
    'position': 'relative',
    'color': '#fff',
    'height': '36px',
    'width': '159px',
    'border-radius': '2px',
    'background-color': '#FC5F3A',
    'max-width': '100%',
    'transition': 'all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1) 0s'
  };
  function Button(style, config, handlers) {
    return new Future(function (resolve) {
      var btnTextOpt = Option.nonEmptyString(config.text);
      var targetOpt = Option.build(config.target);
      var button = btnTextOpt.map(function (btnText) {
        var handleClick = targetOpt.flatMap(function (target) {
          return Option.nonEmptyString(target.href).map(function (href) {
            return redirectOnClick(href, function () {
              handlers && handlers.clickAndTrackAndDisappearPermanently();
            });
          }).orFillWith(function () {
            return Option.nonEmptyString(target.copy).map(function (copyText) {
              var copySuccess = createComponent('p', {
                style: {
                  'text-align': 'center',
                  'margin-bottom': '10px'
                }
              }, [BuiltInIcons.Check(), createComponent('span', {
                style: {
                  'color': '#00CF9B',
                  'font-size': '12px',
                  'margin-left': '2px'
                }
              }, '复制成功')]);
              return function (_, current) {
                var input = document.createElement('input');
                input.value = copyText;
                window.document.body.appendChild(input);
                input.select();
                document.execCommand('copy');
                removeNode(input);
                current.parentElement.insertBefore(copySuccess, current.nextSibling);
                handlers && handlers.clickTargetAndTrack();
              };
            });
          });
        }).orFillWith(function () {
          return Option.build(handlers).map(function (handlers) {
            return handlers.clickAndTrackAndDisappearPermanently;
          });
        });
        return createComponent('button', {
          className: '_gio_c_btn',
          style: __assign({}, buttonStyle, style),
          onClick: handleClick.getOrElse(undefined)
        }, btnText);
      });
      resolve(button);
    });
  }

  var captionStyle = {
    'font-size': '18px',
    'font-weight': '500'
  };
  function Caption(style, config) {
    return Future.successful(function () {
      return Option.nonEmptyString(config.text).map(function (text) {
        return div({
          className: '_gio_c_caption',
          style: __assign({}, captionStyle, style)
        }, text);
      });
    });
  }

  function Img(style, config, handlers) {
    if (!config.src) {
      return Future.successful(None);
    }

    return new Future(function (resolve, reject) {
      var hanldeClick = Option.build(config.target).flatMap(function (_) {
        return Option.nonEmptyString(_.href);
      }).map(function (href) {
        return redirectOnClick(href, function () {
          handlers && handlers.clickAndTrackAndDisappearPermanently();
        });
      }).getOrElse(function () {
        if (config.ctd) {
          handlers && handlers.clickAndTrackAndDisappearPermanently();
        }
      });
      img({
        src: config.src,
        className: '_gio_c_img',
        style: __assign({}, style, {
          cursor: hanldeClick ? 'pointer' : 'auto'
        }),
        onLoad: function onLoad(_, current) {
          current.removeAttribute('width');
          current.removeAttribute('height');
          resolve(Option.build(current));
        },
        onError: function onError(e) {
          reject(new HttpError("Img Load Failed, " + config.src));
        },
        onClick: hanldeClick
      });
    });
  }

  var templateStyle = {
    'gio-modal-anchor-center': {
      'display': 'table-cell',
      'vertical-align': 'middle',
      'text-align': 'center',
      'margin': 0,
      'padding': 0
    },
    'gio-modal-anchor-lb': {
      'bottom': '20px',
      'left': '20px',
      'position': 'fixed',
      'z-index': 2147483647
    },
    'gio-modal-anchor-rb': {
      'bottom': '20px',
      'right': '20px',
      'position': 'fixed',
      'z-index': 2147483647
    }
  };

  var Mask = function Mask() {
    return div({
      id: '_gio_c_modal_mask',
      style: {
        'width': '100%',
        'height': '100%',
        'background': '#000',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        '-moz-opacity': '0.40',
        'opacity': '.40',
        'filter': 'alpha(opacity=40)',
        'z-index': '2147483645',
        '-moz-user-select': 'none',
        '-webkit-user-select': 'none'
      }
    });
  };

  var Outer = function Outer(inner) {
    return div({
      id: 'gio-modal-wrapper-outer',
      style: {
        'width': '100%',
        'height': '100%',
        'display': 'table',
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'z-index': 2147483646
      }
    }, [inner, Mask]);
  };

  var WebTemplateBuilder = function () {
    function WebTemplateBuilder(message) {
      TemplateBuilder.call(this, message);
    }

    WebTemplateBuilder.prototype.build = function (currentHandlers, anchor) {
      var _this = this;

      return this.renderComponent(this.message.contentMetadata, currentHandlers).map(function (modalOpt) {
        return modalOpt.map(function (modal) {
          var inner = div({
            className: _this.className(),
            style: templateStyle[_this.className()]
          }, modal);

          if (_this.position === 'center') {
            var outer = Outer(inner);
            anchor.appendChild(outer);
          } else {
            anchor.appendChild(inner);
          }

          return anchor;
        });
      });
    };

    WebTemplateBuilder.prototype.component2Html = function (component, handlers) {
      var style = component.style;
      var type = component.type;

      switch (type) {
        case 'img':
          return Img(style, component.config, handlers);

        case 'caption':
          return Caption(style, component.config);

        case 'button':
          return Button(style, component.config, handlers);

        case 'paragraph':
          return Paragraph(style, component.config);

        case 'modal':
          return Modal(style, component.config, handlers);

        default:
          return Modal(style, component.config, handlers);
      }
    };

    return WebTemplateBuilder;
  }();

  Extend(TemplateBuilder, WebTemplateBuilder);

  function parseUrl(url) {
    var a = document.createElement('a');
    a.href = url;
    return {
      protocol: a.protocol.replace(':', ''),
      host: a.hostname,
      port: a.port,
      query: a.search,
      params: function () {
        var ret = {},
            seg = a.search.replace(/^\?/, '').split('&'),
            len = seg.length,
            i = 0,
            s;

        for (; i < len; i++) {
          if (!seg[i]) {
            continue;
          }

          s = seg[i].split('=');
          ret[s[0]] = decodeURIComponent(s[1]);
        }

        return ret;
      }(),
      hash: a.hash.replace('#', ''),
      path: a.pathname.replace(/^([^\/])/, '/$1')
    };
  }

  function matchTriggerPage(sourceUrl, triggerPageUrl) {
    if (sourceUrl.length === triggerPageUrl.length && sourceUrl === triggerPageUrl) {
      return true;
    }

    if (sourceUrl[sourceUrl.length - 1] === '?') {
      sourceUrl = sourceUrl.substr(0, sourceUrl.length - 1);
    }

    var parsedSourceUrl = parseUrl(sourceUrl);
    var parsedTriggerPageUrl = parseUrl(triggerPageUrl);

    if (parsedSourceUrl.hash === parsedTriggerPageUrl.hash && parsedSourceUrl.host === parsedTriggerPageUrl.host && parsedSourceUrl.protocol === parsedTriggerPageUrl.protocol && parsedSourceUrl.port === parsedTriggerPageUrl.port && match(parsedSourceUrl.path, parsedTriggerPageUrl.path)) {
      var isParamMatch_1 = true;
      foreach(parsedTriggerPageUrl.params, function (v, k) {
        if (parsedSourceUrl.params[k] !== undefined) {
          isParamMatch_1 = isParamMatch_1 && (parsedSourceUrl.params[k] === v || v === '*');
        } else {
          isParamMatch_1 = false;
        }
      });
      return isParamMatch_1;
    }

    return match(trim(sourceUrl), trim(triggerPageUrl, true));
  }

  function match(source, target) {
    if (source === target) {
      return true;
    }

    var regexpString = target.replace(/\./g, '\\.').replace(/\*/g, '[\/]?.*[\/]?') + '[\/]?';
    var result = source.match(new RegExp(regexpString, 'i'));
    return result !== null && result[0] == result.input;
  }

  function trim(sourceUrl, force) {
    if (force === void 0) {
      force = false;
    }

    sourceUrl = sourceUrl.replace("http://", "").replace("https://", "").trim();
    var lastChar = sourceUrl[sourceUrl.length - 1];

    if (force && lastChar === '/') {
      sourceUrl = sourceUrl.substr(0, sourceUrl.length - 1);
    }

    return sourceUrl;
  }

  function randomNum(minNum, maxNum) {
    switch (arguments.length) {
      case 1:
        return parseInt((Math.random() * minNum + 1).toString(), 10);

      case 2:
        return parseInt((Math.random() * (maxNum - minNum + 1) + minNum).toString(), 10);

      default:
        return 0;
    }
  }

  function getValue(id) {
    return document.getElementById(id).value;
  }

  function renderMessages(_a) {
    var _b = _a.position,
        position = _b === void 0 ? 'center' : _b,
        _c = _a.times,
        times = _c === void 0 ? parseInt(getValue('message-display-times')) : _c,
        _d = _a.message,
        message = _d === void 0 ? popups.popup_1 : _d;
    message = JSON.parse(JSON.stringify(message));
    message.contentMetadata.config.position = position;
    times = times > 0 ? times : 1;

    for (var i = 0; i < times; i++) {
      message = JSON.parse(JSON.stringify(message));
      var randomId = document.getElementById('randomId').checked;

      if (randomId) {
        message.id = randomNum(100, 100000000);
      }

      window['growingio-sdk'].commandQueue.feed({
        type: '1',
        payload: JSON.parse(JSON.stringify(message))
      });
    }
  }

  function renderH5() {
    window['growingio-sdk'].commandQueue.feed({
      type: '1',
      payload: popups.h5
    });
  }

  function clearAllMessages() {
    window['growingio-sdk'].commandQueue.feed({
      type: 'CLEAR_ALL'
    });
  }

  function clearCookie() {
    document.cookie = '';
  }

  function clearLocalStorage() {
    window.localStorage.clear();
  }

  function renderMessagesToDom(id, messageName) {
    var modal = popups[messageName].contentMetadata;
    new WebTemplateBuilder(popups[messageName]).renderComponent(modal).map(function (_) {
      document.getElementById(id).appendChild(_.get());
    });
  }

  window.$$ = {
    clearAllMessages: clearAllMessages,
    renderMessages: renderMessages,
    renderH5: renderH5,
    clearCookie: clearCookie,
    clearLocalStorage: clearLocalStorage,
    renderMessagesToDom: renderMessagesToDom,
    matchTriggerPage: matchTriggerPage
  };

}());
