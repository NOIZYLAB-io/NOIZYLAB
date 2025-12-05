"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.classesP5Sound = exports.classesP5 = void 0;
exports.classesP5 = [
    {
        element: "p5.Color",
        insert: "new p5.Color()",
        code: "new p5.Color()",
        description: "Each color stores the color mode and level maxes that was applied at the time of its construction. These are used to interpret the input arguments (at construction and later for that instance of color) and to format the output e.g. when saturation() is requested.",
        parameters: [],
        fields: [],
        methods: [
            {
                name: "toString()",
                description: "This function returns the color formatted as a string. This can be useful for debugging, or for using p5.js with other libraries.",
            },
            {
                name: "setRed()",
                description: "The setRed function sets the red component of a color. The range depends on your color mode, in the default RGB mode it's between 0 and 255.",
            },
            {
                name: "setGreen()",
                description: "The setGreen function sets the green component of a color. The range depends on your color mode, in the default RGB mode it's between 0 and 255.",
            },
            {
                name: "setBlue()",
                description: "The setBlue function sets the blue component of a color. The range depends on your color mode, in the default RGB mode it's between 0 and 255.",
            },
            {
                name: "setAlpha()",
                description: "The setAlpha function sets the transparency (alpha) value of a color. The range depends on your color mode, in the default RGB mode it's between 0 and 255.",
            },
        ],
    },
    {
        element: "p5.Geometry",
        insert: "new p5.Geometry()",
        code: "new p5.Geometry([detailX], [detailY], [callback])",
        description: "p5 Geometry class",
        parameters: [
            {
                name: "detailX: Integer",
                description: "number of vertices along the x-axis. (Optional)",
            },
            {
                name: "detailY: Integer",
                description: "number of vertices along the y-axis. (Optional)",
            },
            {
                name: "callback: function",
                description: "function to call upon object instantiation. (Optional)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "computeFaces()",
                description: "computes faces for geometry objects based on the vertices.",
            },
            {
                name: "computeNormals()",
                description: "computes smooth normals per vertex as an average of each face.",
            },
            {
                name: "averageNormals()",
                description: "Averages the vertex normals. Used in curved surfaces",
            },
            {
                name: "averagePoleNormals()",
                description: "Averages pole normals. Used in spherical primitives",
            },
            {
                name: "normalize()",
                description: "Modifies all vertices to be centered within the range -100 to 100.",
            },
        ],
    },
    {
        element: "p5.Element",
        insert: "new p5.Element(${1:elt})",
        code: "new p5.Element(elt, [pInst])",
        description: "Base class for all elements added to a sketch, including canvas, graphics buffers, and other HTML elements. It is not called directly, but p5.Element objects are created by calling createCanvas, createGraphics, createDiv, createImg, createInput, etc.",
        parameters: [
            {
                name: "elt: String",
                description: "DOM node that is wrapped",
            },
            {
                name: "pInst: P5",
                description: "pointer to p5 instance (Optional)",
            },
        ],
        fields: [
            {
                name: "elt",
                description: "Underlying HTML element. All normal HTML methods can be called on this.",
            },
        ],
        methods: [
            {
                name: "parent()",
                description: "Attaches the element to the parent specified. A way of setting the container for the element. Accepts either a string ID, DOM node, or p5.Element. If no arguments given, parent node is returned.",
            },
            {
                name: "id()",
                description: "Sets the ID of the element. If no ID argument is passed in, it instead returns the current ID of the element. Note that only one element can have a particular id in a page.",
            },
            {
                name: "class()",
                description: "Adds given class to the element. If no class argument is passed in, it instead returns a string containing the current class(es) of the element.",
            },
            {
                name: "mousePressed()",
                description: "The .mousePressed() function is called once after every time a mouse button is pressed over the element. Some mobile browsers may also trigger this event on a touch screen, if the user performs a quick tap.",
            },
            {
                name: "doubleClicked()",
                description: "The .doubleClicked() function is called once after every time a mouse button is pressed twice over the element. This can be used to attach element and action specific event listeners.",
            },
            {
                name: "mouseWheel()",
                description: "The mouseWheel() function is called once after every time a mouse wheel is scrolled over the element. This can be used to attach element specific event listeners. The function accepts a callback function as argument which will be executed when the wheel event is triggered on the element, the callback function is passed one argument event.",
            },
            {
                name: "mouseReleased()",
                description: "The mouseReleased() function is called once after every time a mouse button is released over the element. Some mobile browsers may also trigger this event on a touch screen, if the user performs a quick tap.",
            },
            {
                name: "mouseClicked()",
                description: "The .mouseClicked() function is called once after a mouse button is pressed and released over the element. Some mobile browsers may also trigger this event on a touch screen, if the user performs a quick tap.",
            },
            {
                name: "mouseMoved()",
                description: "The .mouseMoved() function is called once every time a mouse moves over the element. This can be used to attach an element specific event listener.",
            },
            {
                name: "mouseOver()",
                description: "The .mouseOver() function is called once after every time a mouse moves onto the element. ",
            },
            {
                name: "mouseOut()",
                description: "The .mouseOut() function is called once after every time a mouse moves off the element. This can be used to attach an element specific event listener.",
            },
            {
                name: "touchStarted()",
                description: "The .touchStarted() function is called once after every time a touch is registered. This can be used to attach element specific event listeners.",
            },
            {
                name: "touchMoved()",
                description: "The .touchMoved() function is called once after every time a touch move is registered. This can be used to attach element specific event listeners.",
            },
            {
                name: "touchEnded()",
                description: "The .touchEnded() function is called once after every time a touch is registered. This can be used to attach element specific event listeners.",
            },
            {
                name: "dragOver()",
                description: "The .dragOver() function is called once after every time a file is dragged over the element. This can be used to attach an element specific event listener.",
            },
            {
                name: "dragLeave()",
                description: "The .dragLeave() function is called once after every time a dragged file leaves the element area. This can be used to attach an element specific event listener.",
            },
            {
                name: "addClass()",
                description: "Adds specified class to the element.",
            },
            {
                name: "removeClass()",
                description: "Removes specified class from the element.",
            },
            {
                name: "hasClass()",
                description: "Checks if specified class already set to element",
            },
            {
                name: "toggleClass()",
                description: "Toggles element class",
            },
            {
                name: "child()",
                description: "Attaches the element as a child to the parent specified. Accepts either a string ID, DOM node, or p5.Element. If no argument is specified, an array of children DOM nodes is returned.",
            },
            {
                name: "center()",
                description: "If an argument is given, sets the inner HTML of the element, replacing any existing html. If true is included as a second argument, html is appended instead of replacing existing html. If no arguments are given, returns the inner HTML of the element.",
            },
            {
                name: "position()",
                description: "Sets the position of the element. If no position type argument is given, the position will be relative to (0, 0) of the window. ",
            },
            {
                name: "style()",
                description: "Sets the given style (css) property (1st arg) of the element with the given value (2nd arg). If a single argument is given, .style() returns the value of the given property; however, if the single argument is given in css syntax ('text-align:center'), .style() sets the css appropriately.",
            },
            {
                name: "attribute()",
                description: "Adds a new attribute or changes the value of an existing attribute on the specified element. If no value is specified, returns the value of the given attribute, or null if attribute is not set.",
            },
            {
                name: "removeAttribute()",
                description: "Removes an attribute on the specified element.",
            },
            {
                name: "value()",
                description: "Either returns the value of the element if no arguments given, or sets the value of the element.",
            },
            {
                name: "show()",
                description: "Shows the current element. Essentially, setting display:block for the style.",
            },
            {
                name: "hide()",
                description: " Hides the current element. Essentially, setting display:none for the style.",
            },
            {
                name: "size()",
                description: "Sets the width and height of the element. AUTO can be used to only adjust one dimension at a time. If no arguments are given, it returns the width and height of the element in an object.",
            },
            {
                name: "remove()",
                description: "Removes the element, stops all media streams, and deregisters all listeners.",
            },
            {
                name: "drop()",
                description: "Registers a callback that gets called every time a file that is dropped on the element has been loaded. p5 will load every dropped file into memory and pass it as a p5.File object to the callback.",
            },
        ],
    },
    {
        element: "p5.MediaElement",
        insert: "new p5.MediaElement(${1:elt})",
        code: "new p5.MediaElement(elt)",
        description: "Extends p5.Element to handle audio and video. In addition to the methods of p5.Element, it also contains methods for controlling media. It is not called directly, but p5.MediaElements are created by calling createVideo, createAudio, and createCapture.",
        parameters: [
            {
                name: "elt: String",
                description: "DOM node that is wrapped",
            },
        ],
        fields: [
            {
                name: "src",
                description: "Path to the media element source.",
            },
        ],
        methods: [
            {
                name: "play()",
                description: "Play an HTML5 media element.",
            },
            {
                name: "stop()",
                description: "Stops an HTML5 media element (sets current time to zero).",
            },
            {
                name: "pause()",
                description: "Pauses an HTML5 media element.",
            },
            {
                name: "loop()",
                description: "Set 'loop' to true for an HTML5 media element, and starts playing.",
            },
            {
                name: "noLoop()",
                description: "Set 'loop' to false for an HTML5 media element. Element will stop when it reaches the end.",
            },
            {
                name: "autoplay()",
                description: "Set HTML5 media element to autoplay or not. If no argument is specified, by default it will autoplay.",
            },
            {
                name: "volume()",
                description: "Sets volume for this HTML5 media element. If no argument is given, returns the current volume.",
            },
            {
                name: "speed()",
                description: "If no arguments are given, returns the current playback speed of the element. The speed parameter sets the speed where 2.0 will play the element twice as fast, 0.5 will play at half the speed, and -1 will play the element in normal speed in reverse.",
            },
            {
                name: "time()",
                description: " If no arguments are given, returns the current time of the element. If an argument is given the current time of the element is set to it.",
            },
            {
                name: "duration()",
                description: "Returns the duration of the HTML5 media element.",
            },
            {
                name: "onended()",
                description: "Schedule an event to be called when the audio or video element reaches the end. If the element is looping, this will not be called. The element is passed in as the argument to the onended callback.",
            },
            {
                name: "connect()",
                description: "Send the audio output of this element to a specified audioNode or p5.sound object. If no element is provided, connects to p5's main output. ",
            },
            {
                name: "disconnect()",
                description: "Disconnect all Web Audio routing, including to main output. This is useful if you want to re-route the output through audio effects, for example.",
            },
            {
                name: "showControls()",
                description: "Show the default MediaElement controls, as determined by the web browser.",
            },
            {
                name: "hideControls()",
                description: "Hide the default mediaElement controls.",
            },
            {
                name: "addCue()",
                description: "Schedule events to trigger every time a MediaElement (audio/video) reaches a playback cue point. Accepts a callback function, a time (in seconds) at which to trigger the callback, and an optional parameter for the callback. Time will be passed as the first parameter to the callback function, and param will be the second parameter.",
            },
            {
                name: "removeCue()",
                description: "Remove a callback based on its ID. The ID is returned by the addCue method.",
            },
            {
                name: "clearCues()",
                description: "Remove all of the callbacks that had originally been scheduled via the addCue method.",
            },
        ],
    },
    {
        element: "p5.File",
        insert: "new p5.File(${1:file})",
        code: "new p5.File(file)",
        description: "Base class for a file. Used for Element.drop and createFileInput.",
        parameters: [
            {
                name: "file: File",
                description: "File that is wrapped",
            },
        ],
        fields: [
            {
                name: "file",
                description: "Underlying File object. All normal File methods can be called on this.",
            },
            {
                name: "type",
                description: "File type (image, text, etc.)",
            },
            {
                name: "subtype",
                description: "File subtype (usually the file extension jpg, png, xml, etc.)",
            },
            {
                name: "name",
                description: "File name",
            },
            {
                name: "size",
                description: "File size",
            },
            {
                name: "data",
                description: "URL string containing either image data, the text contents of the file or a parsed object if file is JSON and p5.XML if XML",
            },
        ],
        methods: [],
    },
    {
        element: "p5.Graphics",
        insert: "new p5.Graphics(${1:w}, ${2:h}, ${3:renderer})",
        code: "new p5.Graphics(w, h, renderer, [pInst])",
        description: "Thin wrapper around a renderer, to be used for creating a graphics buffer object. Use this class if you need to draw into an off-screen graphics buffer. The two parameters define the width and height in pixels. The fields and methods for this class are extensive, but mirror the normal drawing API for p5.",
        parameters: [
            {
                name: "w: Number",
                description: "width",
            },
            {
                name: "h: Number",
                description: "height",
            },
            {
                name: "renderer: Constant",
                description: "the renderer to use, either P2D or WEBGL",
            },
            {
                name: "pInst: P5",
                description: "pointer to p5 instance (Optional)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "reset()",
                description: "Resets certain values such as those modified by functions in the Transform category and in the Lights category that are not automatically reset with graphics buffer objects.",
            },
            {
                name: "remove()",
                description: "Removes a Graphics object from the page and frees any resources associated with it.",
            },
        ],
    },
    {
        element: "p5.TypedDict",
        insert: "new p5.TypedDict()",
        code: "new p5.TypedDict()",
        description: "Base class for all p5.Dictionary types. Specifically typed Dictionary classes inherit from this class.",
        parameters: [],
        fields: [],
        methods: [
            {
                name: "size()",
                description: "Returns the number of key-value pairs currently stored in the Dictionary.",
            },
            {
                name: "hasKey()",
                description: "Returns true if the given key exists in the Dictionary, otherwise returns false.",
            },
            {
                name: "get()",
                description: "Returns the value stored at the given key.",
            },
            {
                name: "set()",
                description: "Updates the value associated with the given key in case it already exists in the Dictionary. Otherwise a new key-value pair is added.",
            },
            {
                name: "create()",
                description: "Creates a new key-value pair in the Dictionary.",
            },
            {
                name: "clear()",
                description: "Removes all previously stored key-value pairs from the Dictionary.",
            },
            {
                name: "remove()",
                description: "Removes the key-value pair stored at the given key from the Dictionary.",
            },
            {
                name: "print()",
                description: "Logs the set of items currently stored in the Dictionary to the console.",
            },
            {
                name: "saveTable()",
                description: "Converts the Dictionary into a CSV file for local download.",
            },
            {
                name: "saveJSON()",
                description: "Converts the Dictionary into a JSON file for local download.",
            },
        ],
    },
    {
        element: "p5.NumberDict",
        insert: "new p5.NumberDict()",
        code: "new p5.NumberDict()",
        description: "A simple Dictionary class for Numbers. Extends p5.TypedDict",
        parameters: [],
        fields: [],
        methods: [
            {
                name: "add()",
                description: "Add the given number to the value currently stored at the given key. The sum then replaces the value previously stored in the Dictionary.",
            },
            {
                name: "sub()",
                description: "Subtract the given number from the value currently stored at the given key. The difference then replaces the value previously stored in the Dictionary.",
            },
            {
                name: "mult()",
                description: "Multiply the given number with the value currently stored at the given key. The product then replaces the value previously stored in the Dictionary.",
            },
            {
                name: "div()",
                description: "Divide the given number with the value currently stored at the given key. The quotient then replaces the value previously stored in the Dictionary.",
            },
            {
                name: "minValue()",
                description: "Return the lowest number currently stored in the Dictionary.",
            },
            {
                name: "maxValue()",
                description: "Return the highest number currently stored in the Dictionary.",
            },
            {
                name: "minKey()",
                description: "Return the lowest key currently used in the Dictionary.",
            },
            {
                name: "maxKey()",
                description: "Return the highest key currently used in the Dictionary.",
            },
        ],
    },
    {
        element: "p5.PrintWriter",
        insert: "new p5.PrintWriter()",
        code: "new p5.PrintWriter()",
        description: "p5.PrintWriter",
        parameters: [],
        fields: [],
        methods: [
            {
                name: "write()",
                description: "Writes data to the PrintWriter stream",
            },
            {
                name: "print()",
                description: "Writes data to the PrintWriter stream, and adds a new line at the end",
            },
            {
                name: "clear()",
                description: "Clears the data already written to the PrintWriter object",
            },
            {
                name: "close()",
                description: "Closes the PrintWriter",
            },
        ],
    },
    {
        element: "p5.Font",
        insert: "new p5.Font()",
        code: "new p5.Font([pInst])",
        description: "Base class for font handling",
        parameters: [
            {
                name: "pInst: P5",
                description: "pointer to p5 instance (Optional)",
            },
        ],
        fields: [
            {
                name: "font",
                description: "Underlying opentype font implementation",
            },
        ],
        methods: [
            {
                name: "textBounds()",
                description: "Returns a tight bounding box for the given text string using this font",
            },
            {
                name: "textToPoints()",
                description: "Computes an array of points following the path for specified text",
            },
        ],
    },
    {
        element: "p5.Shader",
        insert: "new p5.Shader(${1:renderer}, ${2:vertSrc}, ${3:fragSrc})",
        code: "new p5.Shader(renderer, vertSrc, fragSrc)",
        description: "Shader class for WEBGL Mode",
        parameters: [
            {
                name: "renderer: p5.RendererGL",
                description: "an instance of p5.RendererGL that will provide the GL context for this new p5.Shader",
            },
            {
                name: "vertSrc: String",
                description: "source code for the vertex shader (as a string)",
            },
            {
                name: "fragSrc: String",
                description: "source code for the fragment shader (as a string)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "setUniform()",
                description: "Used to set the uniforms of a p5.Shader object. Uniforms are used as a way to provide shader programs (which run on the GPU) with values from a sketch (which runs on the CPU).",
            },
        ],
    },
    {
        element: "p5.TableRow",
        insert: "new p5.TableRow()",
        code: "new p5.TableRow([str], [separator])",
        description: "A TableRow object represents a single row of data values, stored in columns, from a table. A Table Row contains both an ordered array, and an unordered JSON object.",
        parameters: [
            {
                name: "str: String",
                description: "optional: populate the row with a string of values, separated by the separator (Optional)",
            },
            {
                name: "separator: String",
                description: "comma separated values (csv) by default (Optional)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "set()",
                description: "Stores a value in the TableRow's specified column. The column may be specified by either its ID or title.",
            },
            {
                name: "setNum()",
                description: "Stores a Float value in the TableRow's specified column. The column may be specified by either its ID or title.",
            },
            {
                name: "setString()",
                description: "Stores a String value in the TableRow's specified column. The column may be specified by either its ID or title.",
            },
            {
                name: "get()",
                description: "Retrieves a value from the TableRow's specified column. The column may be specified by either its ID or title.",
            },
            {
                name: "getNum()",
                description: "Retrieves a Float value from the TableRow's specified column. The column may be specified by either its ID or title.",
            },
            {
                name: "getString()",
                description: "Retrieves an String value from the TableRow's specified column. The column may be specified by either its ID or title.",
            },
        ],
    },
    {
        element: "p5.Image",
        insert: "new p5.Image(${1:width}, ${2:height})",
        code: "new p5.Image(width, height)",
        description: "Creates a new p5.Image. A p5.Image is a canvas backed representation of an image. P5 can display .gif, .jpg and .png images. Images may be displayed in 2D and 3D space. Before an image is used, it must be loaded with the loadImage() function. The p5.Image class contains fields for the width and height of the image, as well as an array called pixels[] that contains the values for every pixel in the image.",
        parameters: [
            {
                name: "width: Number",
                description: "width",
            },
            {
                name: "height: Number",
                description: "height",
            },
        ],
        fields: [
            {
                name: "width",
                description: "Image width.",
            },
            {
                name: "height",
                description: "Image height",
            },
            {
                name: "pixels",
                description: "Array containing the values for all the pixels in the display window. These values are numbers. This array is the size (include an appropriate factor for pixelDensity) of the display window x4, representing the R, G, B, A values in order for each pixel, moving from left to right across each row, then down each column.",
            },
        ],
        methods: [
            {
                name: "loadPixels()",
                description: "Loads the pixels data for this image into the [pixels] attribute.",
            },
            {
                name: "updatePixels()",
                description: "Updates the backing canvas for this image with the contents of the [pixels] array.",
            },
            {
                name: "get()",
                description: "Get a region of pixels from an image. If no params are passed, the whole image is returned. If x and y are the only params passed a single pixel is extracted.",
            },
            {
                name: "set()",
                description: "Set the color of a single pixel or write an image into this p5.Image.",
            },
            {
                name: "resize()",
                description: "Resize the image to a new width and height. To make the image scale proportionally, use 0 as the value for the wide or high parameter.",
            },
            {
                name: "copy()",
                description: "Copies a region of pixels from one image to another. If no srcImage is specified this is used as the source. If the source and destination regions aren't the same size, it will automatically resize source pixels to fit the specified target region.",
            },
            {
                name: "mask()",
                description: "Masks part of an image from displaying by loading another image and using its alpha channel as an alpha channel for this image.",
            },
            {
                name: "filter()",
                description: "Applies an image filter to a p5.Image",
            },
            {
                name: "blend()",
                description: "Copies a region of pixels from one image to another, using a specified blend mode to do the operation.",
            },
            {
                name: "save()",
                description: "Saves the image to a file and force the browser to download it. Accepts two strings for filename and file extension Supports png (default), jpg, and gif",
            },
            {
                name: "reset()",
                description: "Starts an animated GIF over at the beginning state.",
            },
            {
                name: "getCurrentFrame()",
                description: "Gets the index for the frame that is currently visible in an animated GIF.",
            },
            {
                name: "setFrame()",
                description: "Sets the index of the frame that is currently visible in an animated GIF",
            },
            {
                name: "numFrames()",
                description: "Returns the number of frames in an animated GIF",
            },
            {
                name: "play()",
                description: "Plays an animated GIF that was paused with pause()",
            },
            {
                name: "pause()",
                description: "Pauses an animated GIF.",
            },
            {
                name: "delay()",
                description: "Changes the delay between frames in an animated GIF. There is an optional second parameter that indicates an index for a specific frame that should have its delay modified. If no index is given, all frames will have the new delay.",
            },
        ],
    },
    {
        element: "p5.Camera ",
        insert: "new p5.Camera()",
        code: "new p5.Camera()",
        description: "This class describes a camera for use in p5's WebGL mode. It contains camera position, orientation, and projection information necessary for rendering a 3D scene.",
        parameters: [],
        fields: [
            {
                name: "eyeX",
                description: "camera position value on x axis",
            },
            {
                name: "eyeY",
                description: "camera position value on y axis",
            },
            {
                name: "eyeZ",
                description: "camera position value on z axis",
            },
            {
                name: "centerX",
                description: "x coordinate representing center of the sketch",
            },
            {
                name: "centerY",
                description: "y coordinate representing center of the sketch",
            },
            {
                name: "centerZ",
                description: "z coordinate representing center of the sketch",
            },
            {
                name: "upX",
                description: "x component of direction 'up' from camera",
            },
            {
                name: "upY",
                description: "y component of direction 'up' from camera",
            },
            {
                name: "upZ",
                description: "z component of direction 'up' from camera",
            },
        ],
        methods: [
            {
                name: "perspective()",
                description: "Sets a perspective projection. Accepts the same parameters as the global perspective().",
            },
            {
                name: "ortho()",
                description: "Sets an orthographic projection. Accepts the same parameters as the global ortho().",
            },
            {
                name: "frustum()",
                description: "Sets the camera's frustum. Accepts the same parameters as the global frustum().",
            },
            {
                name: "pan()",
                description: " Panning rotates the camera view to the left and right.",
            },
            {
                name: "tilt()",
                description: "Tilting rotates the camera view up and down.",
            },
            {
                name: "lookAt()",
                description: "Reorients the camera to look at a position in world space.",
            },
            {
                name: "camera()",
                description: "Sets the camera's position and orientation. Accepts the same parameters as the global camera().",
            },
            {
                name: "move()",
                description: "Move camera along its local axes while maintaining current camera orientation.",
            },
            {
                name: "setPosition()",
                description: "Set camera position in world-space while maintaining current camera orientation.",
            },
        ],
    },
    {
        element: "p5.XML ",
        insert: "new p5.XML()",
        code: "new p5.XML()",
        description: "XML is a representation of an XML object, able to parse XML code. Use loadXML() to load external XML files and create XML objects.",
        parameters: [],
        fields: [],
        methods: [
            {
                name: "getParent()",
                description: "Gets a copy of the element's parent. Returns the parent as another p5.XML object.",
            },
            {
                name: "getName()",
                description: "Gets the element's full name, which is returned as a String.",
            },
            {
                name: "setName()",
                description: "Sets the element's name, which is specified as a String.",
            },
            {
                name: "hasChildren()",
                description: "Checks whether or not the element has any children, and returns the result as a boolean. ",
            },
            {
                name: "listChildren()",
                description: " Get the names of all of the element's children, and returns the names as an array of Strings. This is the same as looping through and calling getName() on each child element individually.",
            },
            {
                name: "getChildren()",
                description: "Returns all of the element's children as an array of p5.XML objects.",
            },
            {
                name: "getChild()",
                description: "Returns the first of the element's children that matches the name parameter or the child of the given index.It returns undefined if no matching child is found.",
            },
            {
                name: "addChild()",
                description: "Appends a new child to the element. The child can be specified with either a String, which will be used as the new tag's name, or as a reference to an existing p5.XML object. ",
            },
            {
                name: "removeChild()",
                description: "Removes the element specified by name or index.",
            },
            {
                name: "getAttributeCount()",
                description: "Counts the specified element's number of attributes, returned as an Number.",
            },
            {
                name: "listAttributes()",
                description: "Gets all of the specified element's attributes, and returns them as an array of Strings.",
            },
            {
                name: "hasAttribute()",
                description: "Checks whether or not an element has the specified attribute.",
            },
            {
                name: "getNum()",
                description: "Returns an attribute value of the element as an Number.",
            },
            {
                name: "getString()",
                description: "Returns an attribute value of the element as an String.",
            },
            {
                name: "setAttribute()",
                description: "Sets the content of an element's attribute. The first parameter specifies the attribute name, while the second specifies the new content.",
            },
            {
                name: "getContent()",
                description: "Returns the content of an element. If there is no such content, defaultValue is returned if specified, otherwise null is returned.",
            },
            {
                name: "setContent()",
                description: "Sets the element's content.",
            },
            {
                name: "serialize()",
                description: "Serializes the element into a string. This function is useful for preparing the content to be sent over a http request or saved to file.",
            },
        ],
    },
    {
        element: "p5.Table ",
        insert: "new p5.Table()",
        code: "new p5.Table([rows])",
        description: "Table objects store data with multiple rows and columns, much like in a traditional spreadsheet. Tables can be generated from scratch, dynamically, or using data from an existing file.",
        parameters: [
            {
                name: "rows: p5.TableRow[]",
                description: "An array of p5.TableRow objects (Optional)",
            },
        ],
        fields: [
            {
                name: "columns",
                description: "An array containing the names of the columns in the table, if the header the table is loaded with the header parameter.",
            },
            {
                name: "rows",
                description: "An array containing the p5.TableRow objects that make up the rows of the table. The same result as calling getRows()",
            },
        ],
        methods: [
            {
                name: "addRow()",
                description: "Use addRow() to add a new row of data to a p5.Table object.",
            },
            {
                name: "removeRow()",
                description: "Removes a row from the table object.",
            },
            {
                name: "getRow()",
                description: "Returns a reference to the specified p5.TableRow.",
            },
            {
                name: "getRows()",
                description: "Gets all rows from the table. Returns an array of p5.TableRows.",
            },
            {
                name: "findRow()",
                description: "Finds the first row in the Table that contains the value provided, and returns a reference to that row. Even if multiple rows are possible matches, only the first matching row is returned.",
            },
            {
                name: "findRows()",
                description: "Finds the rows in the Table that contain the value provided, and returns references to those rows. Returns an Array, so for must be used to iterate through all the rows, as shown in the example above.",
            },
            {
                name: "matchRow()",
                description: "Finds the first row in the Table that matches the regular expression provided, and returns a reference to that row. Even if multiple rows are possible matches, only the first matching row is returned. ",
            },
            {
                name: "matchRows()",
                description: "Finds the rows in the Table that match the regular expression provided, and returns references to those rows. Returns an array, so for must be used to iterate through all the rows, as shown in the example. ",
            },
            {
                name: "getColumn()",
                description: "Retrieves all values in the specified column, and returns them as an array.",
            },
            {
                name: "clearRows()",
                description: "Removes all rows from a Table. While all rows are removed, columns and column titles are maintained.",
            },
            {
                name: "addColumn()",
                description: "Use addColumn() to add a new column to a Table object.",
            },
            {
                name: "getColumnCount()",
                description: "Returns the total number of columns in a Table",
            },
            {
                name: "getRowCount()",
                description: "Returns the total number of rows in a Table.",
            },
            {
                name: "removeTokens()",
                description: "Removes any of the specified characters (or tokens).",
            },
            {
                name: "trim()",
                description: "Trims leading and trailing whitespace, such as spaces and tabs, from String table values.",
            },
            {
                name: "removeColumn()",
                description: "Use removeColumn() to remove an existing column from a Table object.",
            },
            {
                name: "set()",
                description: " Stores a value in the Table's specified row and column. ",
            },
            {
                name: "setNum()",
                description: "Stores a Float value in the Table's specified row and column. ",
            },
            {
                name: "setString()",
                description: " Stores a String value in the Table's specified row and column.",
            },
            {
                name: "get()",
                description: "Retrieves a value from the Table's specified row and column. ",
            },
            {
                name: "getNum()",
                description: " Retrieves a Float value from the Table's specified row and column.",
            },
            {
                name: "getString()",
                description: " Retrieves a String value from the Table's specified row and column.",
            },
            {
                name: "getObject()",
                description: "Retrieves all table data and returns as an object. If a column name is passed in, each row object will be stored with that attribute as its title.",
            },
            {
                name: "getArray()",
                description: "Retrieves all table data and returns it as a multidimensional array.",
            },
        ],
    },
    {
        element: "p5.VectorNew",
        insert: "new p5.Vector()",
        code: "new p5.Vector([x], [y], [z])",
        description: "A class to describe a two or three dimensional vector, specifically a Euclidean (also known as geometric) vector. A vector is an entity that has both magnitude and direction. The datatype, however, stores the components of the vector (x, y for 2D, and x, y, z for 3D).",
        parameters: [
            {
                name: "x: Number",
                description: "x component of the vector (Optional)",
            },
            {
                name: "y: Number",
                description: "y component of the vector (Optional)",
            },
            {
                name: "z: Number",
                description: "z component of the vector (Optional)",
            },
        ],
        fields: [
            {
                name: "x",
                description: "The x component of the vector",
            },
            {
                name: "y",
                description: "The y component of the vector",
            },
            {
                name: "z",
                description: "The z component of the vector",
            },
        ],
        methods: [
            {
                name: "toString()",
                description: "Returns a string representation of a vector v by calling String(v) or v.toString(). ",
            },
            {
                name: "set()",
                description: "Sets the x, y, and z component of the vector using two or three separate variables, the data from a p5.Vector, or the values from a float array.",
            },
            {
                name: "copy()",
                description: "Gets a copy of the vector, returns a p5.Vector object.",
            },
            {
                name: "add()",
                description: "Adds x, y, and z components to a vector, adds one vector to another, or adds two independent vectors together.",
            },
            {
                name: "rem()",
                description: "Gives remainder of a vector when it is divided by another vector.",
            },
            {
                name: "sub()",
                description: "Subtracts x, y, and z components from a vector, subtracts one vector from another, or subtracts two independent vectors.",
            },
            {
                name: "mult()",
                description: "Multiplies the vector by a scalar, multiplies the x, y, and z components from a vector, or multiplies the x, y, and z components of two independent vectors.",
            },
            {
                name: "div()",
                description: " Divides the vector by a scalar, divides a vector by the x, y, and z arguments, or divides the x, y, and z components of two vectors against each other.",
            },
            {
                name: "mag()",
                description: "Calculates the magnitude (length) of the vector and returns the result as a float",
            },
            {
                name: "magSq()",
                description: "Calculates the squared magnitude of the vector and returns the result as a float",
            },
            {
                name: "dot()",
                description: "Calculates the dot product of two vectors. The version of the method that computes the dot product of two independent vectors is a static method.",
            },
            {
                name: "cross()",
                description: "Calculates and returns a vector composed of the cross product between two vectors. ",
            },
            {
                name: "dist()",
                description: "Calculates the Euclidean distance between two points (considering a point as a vector object).",
            },
            {
                name: "normalize()",
                description: "Normalize the vector to length 1 (make it a unit vector).",
            },
            {
                name: "limit()",
                description: "Limit the magnitude of this vector to the value used for the max parameter.",
            },
            {
                name: "setMag()",
                description: "Set the magnitude of this vector to the value used for the len parameter.",
            },
            {
                name: "heading()",
                description: "Calculate the angle of rotation for this vector(only 2D vectors).",
            },
            {
                name: "setHeading()",
                description: "Rotate the vector to a specific angle (only 2D vectors), magnitude remains the same",
            },
            {
                name: "rotate()",
                description: "Rotate the vector by an angle (only 2D vectors), magnitude remains the same",
            },
            {
                name: "angleBetween()",
                description: "Calculates and returns the angle between two vectors.",
            },
            {
                name: "lerp()",
                description: " Linear interpolate the vector to another vector",
            },
            {
                name: "reflect()",
                description: "Reflect the incoming vector about a normal to a line in 2D, or about a normal to a plane in 3D This method acts on the vector directly",
            },
            {
                name: "array()",
                description: "Return a representation of this vector as a float array.",
            },
            {
                name: "equals()",
                description: "Equality check against a p5.Vector",
            },
            {
                name: "fromAngle()",
                description: "Make a new 2D vector from an angle",
            },
            {
                name: "fromAngles()",
                description: "Make a new 3D vector from a pair of ISO spherical angles",
            },
            {
                name: "random2D()",
                description: "Make a new 2D unit vector from a random angle",
            },
            {
                name: "random3D()",
                description: "Make a new random 3D unit vector.",
            },
        ],
    },
    {
        element: "p5.Vector",
        insert: "p5.Vector",
        code: "p5.Vector",
        description: "A class to describe a two or three dimensional vector, specifically a Euclidean (also known as geometric) vector. A vector is an entity that has both magnitude and direction. The datatype, however, stores the components of the vector (x, y for 2D, and x, y, z for 3D).",
        parameters: [],
        fields: [],
        methods: [
            {
                name: "toString()",
                description: "Returns a string representation of a vector v by calling String(v) or v.toString(). ",
            },
            {
                name: "set()",
                description: "Sets the x, y, and z component of the vector using two or three separate variables, the data from a p5.Vector, or the values from a float array.",
            },
            {
                name: "copy()",
                description: "Gets a copy of the vector, returns a p5.Vector object.",
            },
            {
                name: "add()",
                description: "Adds x, y, and z components to a vector, adds one vector to another, or adds two independent vectors together.",
            },
            {
                name: "rem()",
                description: "Gives remainder of a vector when it is divided by another vector.",
            },
            {
                name: "sub()",
                description: "Subtracts x, y, and z components from a vector, subtracts one vector from another, or subtracts two independent vectors.",
            },
            {
                name: "mult()",
                description: "Multiplies the vector by a scalar, multiplies the x, y, and z components from a vector, or multiplies the x, y, and z components of two independent vectors.",
            },
            {
                name: "div()",
                description: " Divides the vector by a scalar, divides a vector by the x, y, and z arguments, or divides the x, y, and z components of two vectors against each other.",
            },
            {
                name: "mag()",
                description: "Calculates the magnitude (length) of the vector and returns the result as a float",
            },
            {
                name: "magSq()",
                description: "Calculates the squared magnitude of the vector and returns the result as a float",
            },
            {
                name: "dot()",
                description: "Calculates the dot product of two vectors. The version of the method that computes the dot product of two independent vectors is a static method.",
            },
            {
                name: "cross()",
                description: "Calculates and returns a vector composed of the cross product between two vectors. ",
            },
            {
                name: "dist()",
                description: "Calculates the Euclidean distance between two points (considering a point as a vector object).",
            },
            {
                name: "normalize()",
                description: "Normalize the vector to length 1 (make it a unit vector).",
            },
            {
                name: "limit()",
                description: "Limit the magnitude of this vector to the value used for the max parameter.",
            },
            {
                name: "setMag()",
                description: "Set the magnitude of this vector to the value used for the len parameter.",
            },
            {
                name: "heading()",
                description: "Calculate the angle of rotation for this vector(only 2D vectors).",
            },
            {
                name: "setHeading()",
                description: "Rotate the vector to a specific angle (only 2D vectors), magnitude remains the same",
            },
            {
                name: "rotate()",
                description: "Rotate the vector by an angle (only 2D vectors), magnitude remains the same",
            },
            {
                name: "angleBetween()",
                description: "Calculates and returns the angle between two vectors.",
            },
            {
                name: "lerp()",
                description: " Linear interpolate the vector to another vector",
            },
            {
                name: "reflect()",
                description: "Reflect the incoming vector about a normal to a line in 2D, or about a normal to a plane in 3D This method acts on the vector directly",
            },
            {
                name: "array()",
                description: "Return a representation of this vector as a float array.",
            },
            {
                name: "equals()",
                description: "Equality check against a p5.Vector",
            },
            {
                name: "fromAngle()",
                description: "Make a new 2D vector from an angle",
            },
            {
                name: "fromAngles()",
                description: "Make a new 3D vector from a pair of ISO spherical angles",
            },
            {
                name: "random2D()",
                description: "Make a new 2D unit vector from a random angle",
            },
            {
                name: "random3D()",
                description: "Make a new random 3D unit vector.",
            },
        ],
    },
];
exports.classesP5Sound = [
    {
        element: "p5.Score",
        insert: "new p5.Score()",
        code: "new p5.Score([parts])",
        description: "A Score consists of a series of Parts. The parts will be played back in order.",
        parameters: [
            {
                name: "parts: p5.Part",
                description: "One or multiple parts, to be played in sequence. (Optional)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "start()",
                description: "Start playback of the score.",
            },
            {
                name: "stop()",
                description: "Stop playback of the score.",
            },
            {
                name: "pause()",
                description: "Pause playback of the score.",
            },
            {
                name: "loop()",
                description: "Loop playback of the score.",
            },
            {
                name: "noLoop()",
                description: "Stop looping playback of the score. If it is currently playing, this will go into effect after the current round of playback completes.",
            },
            {
                name: "setBPM()",
                description: "Set the tempo for all parts in the score",
            },
        ],
    },
    {
        element: "p5.Part",
        insert: "new p5.Part()",
        code: "new p5.Part([steps] [tatums])",
        description: "A p5.Part plays back one or more p5.Phrases. Instantiate a part with steps and tatums. By default, each step represents a 1/16th note.",
        parameters: [
            {
                name: "steps: Number",
                description: "Steps in the part (Optional)",
            },
            {
                name: "tatums: Number",
                description: "Divisions of a beat, e.g. use 1/4, or 0.25 for a quater note (default is 1/16, a sixteenth note) (Optional)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "setBPM()",
                description: "Set the tempo of this part, in Beats Per Minute.",
            },
            {
                name: "getBPM()",
                description: "Returns the tempo, in Beats Per Minute, of this part.",
            },
            {
                name: "start()",
                description: "Start playback of this part. It will play through all of its phrases at a speed determined by setBPM.",
            },
            {
                name: "loop()",
                description: "Loop playback of this part. It will begin looping through all of its phrases at a speed determined by setBPM.",
            },
            {
                name: "noLoop()",
                description: "Tell the part to stop looping.",
            },
            {
                name: "stop()",
                description: "Stop the part and cue it to step 0. Playback will resume from the begining of the Part when it is played again.",
            },
            {
                name: "pause()",
                description: "Pause the part. Playback will resume from the current step.",
            },
            {
                name: "addPhrase()",
                description: "Add a p5.Phrase to this Part.",
            },
            {
                name: "removePhrase()",
                description: "Remove a phrase from this part, based on the name it was given when it was created.",
            },
            {
                name: "getPhrase()",
                description: "Get a phrase from this part, based on the name it was given when it was created. Now you can modify its array.",
            },
            {
                name: "replaceSequence()",
                description: "Find all sequences with the specified name, and replace their patterns with the specified array.",
            },
            {
                name: "onStep()",
                description: "Set the function that will be called at every step. This will clear the previous function.",
            },
        ],
    },
    {
        element: "p5.Phrase",
        insert: "new p5.Phrase(${1:name}, ${2:callback}, ${3:sequence})",
        code: "new p5.Phrase(name, callback, sequence)",
        description: "A phrase is a pattern of musical events over time, i.e. a series of notes and rests. Phrases must be added to a p5.Part for playback, and each part can play multiple phrases at the same time. ",
        parameters: [
            {
                name: "name: String",
                description: "Name so that you can access the Phrase.",
            },
            {
                name: "callback: function",
                description: "The name of a function that this phrase will call. Typically it will play a sound, and accept two parameters: a time at which to play the sound (in seconds from now), and a value from the sequence array.",
            },
            {
                name: "sequence: Array",
                description: "Array of values to pass into the callback at each step of the phrase.",
            },
        ],
        fields: [
            {
                name: "sequence",
                description: "Array of values to pass into the callback at each step of the phrase. Depending on the callback function's requirements, these values may be numbers, strings, or an object with multiple parameters. Zero (0) indicates a rest.",
            },
        ],
        methods: [],
    },
    {
        element: "p5.SoundLoop",
        insert: "new p5.SoundLoop(${1:callback})",
        code: "new p5.SoundLoop(callback, [interval])",
        description: "SoundLoop",
        parameters: [
            {
                name: "callback: function",
                description: "this function will be called on each iteration of theloop",
            },
            {
                name: "interval: Number|String",
                description: "amount of time (if a number) or beats (if a string, following Tone.Time convention) for each iteration of the loop. Defaults to 1 second. (Optional)",
            },
        ],
        fields: [
            {
                name: "bpm",
                description: "Getters and Setters, setting any paramter will result in a change in the clock's frequency, that will be reflected after the next callback beats per minute (defaults to 60)",
            },
            {
                name: "timeSignature",
                description: "number of quarter notes in a measure (defaults to 4)",
            },
            {
                name: "interval",
                description: "length of the loops interval",
            },
            {
                name: "iterations",
                description: "how many times the callback has been called so far",
            },
            {
                name: "musicalTimeMode",
                description: "musicalTimeMode uses Tone.Time convention true if string, false if number",
            },
            {
                name: "maxIterations",
                description: "Set a limit to the number of loops to play. defaults to Infinity",
            },
        ],
        methods: [
            {
                name: "start()",
                description: "Start the loop",
            },
            {
                name: "stop()",
                description: "Stop the loop",
            },
            {
                name: "pause()",
                description: "Pause the loop",
            },
            {
                name: "syncedStart()",
                description: "Synchronize loops. Use this method to start two or more loops in synchronization or to start a loop in synchronization with a loop that is already playing.",
            },
        ],
    },
    {
        element: "p5.SoundRecorder",
        insert: "new p5.SoundRecorder()",
        code: "new p5.SoundRecorder()",
        description: "Record sounds for playback and/or to save as a .wav file. The p5.SoundRecorder records all sound output from your sketch, or can be assigned a specific source with setInput().",
        parameters: [],
        fields: [],
        methods: [
            {
                name: "setInput()",
                description: "Connect a specific device to the p5.SoundRecorder. If no parameter is given, p5.SoundRecorer will record all audible p5.sound from your sketch.",
            },
            {
                name: "record()",
                description: "Start recording. To access the recording, provide a p5.SoundFile as the first parameter. The p5.SoundRecorder will send its recording to that p5.SoundFile for playback once recording is complete.",
            },
            {
                name: "stop()",
                description: "Stop the recording. Once the recording is stopped, the results will be sent to the p5.SoundFile that was given on .record(), and if a callback function was provided on record, that function will be called.",
            },
        ],
    },
    {
        element: "p5.Reverb",
        insert: "new p5.Reverb()",
        code: "new p5.Reverb()",
        description: "Reverb adds depth to a sound through a large number of decaying echoes. It creates the perception that sound is occurring in a physical space. The p5.Reverb has paramters for Time (how long does the reverb last) and decayRate (how much the sound decays with each echo) that can be set with the .set() or .process() methods.",
        parameters: [],
        fields: [],
        methods: [
            {
                name: "process()",
                description: "Connect a source to the reverb, and assign reverb parameters.",
            },
            {
                name: "set()",
                description: "Set the reverb settings. Similar to .process(), but without assigning a new input.",
            },
            {
                name: "amp()",
                description: "Set the output level of the reverb effect.",
            },
            {
                name: "connect()",
                description: "Send output to a p5.sound or web audio object",
            },
            {
                name: "disconnect()",
                description: "Disconnect all output.",
            },
        ],
    },
    {
        element: "p5.Convolver",
        insert: "new p5.Convolver(${1:path})",
        code: "new p5.Convolver(path, [callback], [errorCallback])",
        description: "p5.Convolver extends p5.Reverb. It can emulate the sound of real physical spaces through a process called convolution. Convolution multiplies any audio input by an impulse response to simulate the dispersion of sound over time. The impulse response is generated from an audio file that you provide. One way to generate an impulse response is to pop a balloon in a reverberant space and record the echo. Convolution can also be used to experiment with sound.",
        parameters: [
            {
                name: "path: String",
                description: "path to a sound file",
            },
            {
                name: "callback: function",
                description: "function to call when loading succeeds (Optional)",
            },
            {
                name: "errorCallback: function",
                description: "function to call if loading fails. This function will receive an error or XMLHttpRequest object with information about what went wrong. (Optional)",
            },
        ],
        fields: [
            {
                name: "convolverNode",
                description: "Internally, the p5.Convolver uses the a Web Audio Convolver Node.",
            },
            {
                name: "impulses",
                description: "If you load multiple impulse files using the .addImpulse method, they will be stored as Objects in this Array.",
            },
        ],
        methods: [
            {
                name: "process()",
                description: "Connect a source to the convolver.",
            },
            {
                name: "addImpulse()",
                description: "Load and assign a new Impulse Response to the p5.Convolver. The impulse is added to the .impulses array.",
            },
            {
                name: "resetImpulse()",
                description: "Similar to .addImpulse, except that the .impulses Array is reset to save memory. ",
            },
            {
                name: "toggleImpulse()",
                description: "If you have used .addImpulse() to add multiple impulses to a p5.Convolver, then you can use this method to toggle between the items in the .impulses Array. Accepts a parameter to identify which impulse you wish to use, identified either by its original filename (String) or by its position in the .impulses Array (Number).",
            },
        ],
    },
    {
        element: "p5.Filter",
        insert: "new p5.Filter()",
        code: "new p5.Filter([type])",
        description: "A p5.Filter uses a Web Audio Biquad Filter to filter the frequency response of an input source.",
        parameters: [
            {
                name: "type: String",
                description: "'lowpass' (default), 'highpass', 'bandpass' (Optional)",
            },
        ],
        fields: [
            {
                name: "biquadFilter",
                description: "The p5.Filter is built with a Web Audio BiquadFilter Node.",
            },
        ],
        methods: [
            {
                name: "process()",
                description: "Filter an audio signal according to a set of filter parameters.",
            },
            {
                name: "set()",
                description: "Set the frequency and the resonance of the filter.",
            },
            {
                name: "freq()",
                description: "Set the filter frequency, in Hz, from 10 to 22050 (the range of human hearing, although in reality most people hear in a narrower range).",
            },
            {
                name: "res()",
                description: "Controls either width of a bandpass frequency, or the resonance of a low/highpass cutoff frequency.",
            },
            {
                name: "gain()",
                description: "Controls the gain attribute of a Biquad Filter. This is distinctly different from .amp() which is inherited from p5.Effect .amp() controls the volume via the output gain node p5.Filter.gain() controls the gain parameter of a Biquad Filter node.",
            },
            {
                name: "toggle()",
                description: "Toggle function. Switches between the specified type and allpass",
            },
            {
                name: "setType()",
                description: "Set the type of a p5.Filter. Possible types include: lowpass (default), highpass, bandpass, lowshelf, highshelf, peaking, notch, allpass.",
            },
        ],
    },
    {
        element: "p5.Delay",
        insert: "new p5.Delay()",
        code: "new p5.Delay()",
        description: "Delay is an echo effect. It processes an existing sound source, and outputs a delayed version of that sound. The p5.Delay can produce different effects depending on the delayTime, feedback, filter, and type. In the example below, a feedback of 0.5 (the default value) will produce a looping delay that decreases in volume by 50% each repeat.",
        parameters: [],
        fields: [
            {
                name: "leftDelay",
                description: "The p5.Delay is built with two Web Audio Delay Nodes, one for each stereo channel.",
            },
            {
                name: "rightDelay",
                description: "The p5.Delay is built with two Web Audio Delay Nodes, one for each stereo channel.",
            },
        ],
        methods: [
            {
                name: "process()",
                description: "Add delay to an audio signal according to a set of delay parameters.",
            },
            {
                name: "delayTime()",
                description: "Set the delay (echo) time, in seconds. Usually this value will be a floating point number between 0.0 and 1.0.",
            },
            {
                name: "feedback()",
                description: "Feedback occurs when Delay sends its signal back through its input in a loop. The feedback amount determines how much signal to send each time through the loop.",
            },
            {
                name: "filter()",
                description: "Set a lowpass filter frequency for the delay. A lowpass filter will cut off any frequencies higher than the filter frequency.",
            },
            {
                name: "setType()",
                description: "Choose a preset type of delay. 'pingPong' bounces the signal from the left to the right channel to produce a stereo effect.",
            },
            {
                name: "amp()",
                description: " Set the output level of the delay effect.",
            },
            {
                name: "connect()",
                description: "Send output to a p5.sound or web audio object",
            },
            {
                name: "disconnect()",
                description: "Disconnect all output.",
            },
        ],
    },
    {
        element: "p5.Envelope",
        insert: "new p5.Envelope()",
        code: "new p5.Envelope()",
        description: "Envelopes are pre-defined amplitude distribution over time. Typically, envelopes are used to control the output volume of an object, a series of fades referred to as Attack, Decay, Sustain and Release ( ADSR ). Envelopes can also control other Web Audio Parameters—for example, a p5.Envelope can control an Oscillator's frequency like this: osc.freq(env).",
        parameters: [],
        fields: [
            {
                name: "attackTime",
                description: "Time until envelope reaches attackLevel",
            },
            {
                name: "attackLevel",
                description: "Level once attack is complete",
            },
            {
                name: "decayTime",
                description: "Time until envelope reaches decayLevel.",
            },
            {
                name: "decayLevel",
                description: " Level after decay. The envelope will sustain here until it is released.",
            },
            {
                name: "releaseTime",
                description: "Duration of the release portion of the envelope.",
            },
            {
                name: "releaseLevel",
                description: "Level at the end of the release.",
            },
        ],
        methods: [
            {
                name: "set()",
                description: "Reset the envelope with a series of time/value pairs.",
            },
            {
                name: "setADSR()",
                description: "Set values like a traditional ADSR envelope .",
            },
            {
                name: "setRange()",
                description: "Set max (attackLevel) and min (releaseLevel) of envelope.",
            },
            {
                name: "setInput()",
                description: "Assign a parameter to be controlled by this envelope. If a p5.Sound object is given, then the p5.Envelope will control its output gain. If multiple inputs are provided, the env will control all of them.",
            },
            {
                name: "setExp()",
                description: "Set whether the envelope ramp is linear (default) or exponential. Exponential ramps can be useful because we perceive amplitude and frequency logarithmically.",
            },
            {
                name: "play()",
                description: "Play tells the envelope to start acting on a given input.",
            },
            {
                name: "triggerAttack()",
                description: "Trigger the Attack, and Decay portion of the Envelope. ",
            },
            {
                name: "triggerRelease()",
                description: "Trigger the Release of the Envelope. This is similar to releasing the key on a piano and letting the sound fade according to the release level and release time.",
            },
            {
                name: "ramp()",
                description: "Exponentially ramp to a value using the first two values from setADSR(attackTime, decayTime) as time constants for simple exponential ramps.",
            },
            {
                name: "add()",
                description: "Add a value to the p5.Oscillator's output amplitude, and return the oscillator.",
            },
            {
                name: "mult()",
                description: "Multiply the p5.Envelope's output amplitude by a fixed value.",
            },
            {
                name: "scale()",
                description: "Scale this envelope's amplitude values to a given range, and return the envelope.",
            },
        ],
    },
    {
        element: "p5.MonoSynth",
        insert: "new p5.MonoSynth()",
        code: "new p5.MonoSynth()",
        description: "A MonoSynth is used as a single voice for sound synthesis. This is a class to be used in conjunction with the PolySynth class. Custom synthetisers should be built inheriting from this class.",
        parameters: [],
        fields: [
            {
                name: "attack",
                description: "Getters and Setters",
            },
            {
                name: "decay",
                description: "Getters and Setters",
            },
            {
                name: "sustain",
                description: "Getters and Setters",
            },
            {
                name: "release",
                description: "Getters and Setters",
            },
        ],
        methods: [
            {
                name: "play()",
                description: "Play tells the MonoSynth to start playing a note. This method schedules the calling of .triggerAttack and .triggerRelease.",
            },
            {
                name: "triggerAttack()",
                description: "Trigger the Attack, and Decay portion of the Envelope. Similar to holding down a key on a piano, but it will hold the sustain level until you let go.",
            },
            {
                name: "triggerRelease()",
                description: "Trigger the release of the Envelope. This is similar to releasing the key on a piano and letting the sound fade according to the release level and release time.",
            },
            {
                name: "setADSR()",
                description: "Set values like a traditional ADSR envelope .",
            },
            {
                name: "amp()",
                description: "MonoSynth amp",
            },
            {
                name: "connect()",
                description: "Connect to a p5.sound / Web Audio object.",
            },
            {
                name: "disconnect()",
                description: "Disconnect all outputs",
            },
            {
                name: "dispose()",
                description: "Get rid of the MonoSynth and free up its resources / memory.",
            },
        ],
    },
    {
        element: "p5.PolySynth",
        insert: "new p5.PolySynth()",
        code: "new p5.PolySynth([synthVoice], [maxVoices])",
        description: "An AudioVoice is used as a single voice for sound synthesis. The PolySynth class holds an array of AudioVoice, and deals with voices allocations, with setting notes to be played, and parameters to be set.",
        parameters: [
            {
                name: "synthVoice: Number",
                description: "A monophonic synth voice inheriting the AudioVoice class. Defaults to p5.MonoSynth (Optional)",
            },
            {
                name: "maxVoices: Number",
                description: "Number of voices, defaults to 8; (Optional)",
            },
        ],
        fields: [
            {
                name: "notes",
                description: "An object that holds information about which notes have been played and which notes are currently being played. New notes are added as keys on the fly.",
            },
            {
                name: "polyvalue",
                description: "A PolySynth must have at least 1 voice, defaults to 8",
            },
            {
                name: "AudioVoice",
                description: "Monosynth that generates the sound for each note that is triggered. The p5.PolySynth defaults to using the p5.MonoSynth as its voice.",
            },
        ],
        methods: [
            {
                name: "play()",
                description: " Play a note by triggering noteAttack and noteRelease with sustain time",
            },
            {
                name: "noteADSR()",
                description: "noteADSR sets the envelope for a specific note that has just been triggered. Using this method modifies the envelope of whichever audiovoice is being used to play the desired note.",
            },
            {
                name: "setADSR()",
                description: "Set the PolySynths global envelope. This method modifies the envelopes of each monosynth so that all notes are played with this envelope.",
            },
            {
                name: "noteAttack()",
                description: "Trigger the Attack, and Decay portion of a MonoSynth. Similar to holding down a key on a piano, but it will hold the sustain level until you let go.",
            },
            {
                name: "noteRelease()",
                description: " Trigger the Release of an AudioVoice note. This is similar to releasing the key on a piano and letting the sound fade according to the release level and release time.",
            },
            {
                name: "connect()",
                description: "Connect to a p5.sound / Web Audio object.",
            },
            {
                name: "disconnect()",
                description: "Disconnect all outputs",
            },
            {
                name: "dispose()",
                description: "Get rid of the MonoSynth and free up its resources / memory",
            },
        ],
    },
    {
        element: "p5.Pulse",
        insert: "new p5.Pulse()",
        code: "new p5.Pulse([freq], [w])",
        description: "Creates a Pulse object, an oscillator that implements Pulse Width Modulation. The pulse is created with two oscillators. Accepts a parameter for frequency, and to set the width between the pulses.",
        parameters: [
            {
                name: "freq: Number",
                description: "Frequency in oscillations per second (Hz) (Optional)",
            },
            {
                name: "w: Number",
                description: "Width between the pulses (0 to 1.0, defaults to 0) (Optional)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "width()",
                description: "Set the width of a Pulse object (an oscillator that implements Pulse Width Modulation).",
            },
        ],
    },
    {
        element: "p5.Noise",
        insert: "new p5.Noise(${1:type})",
        code: "new p5.Noise()",
        description: "Noise is a type of oscillator that generates a buffer with random values.",
        parameters: [
            {
                name: "type: String",
                description: "Type of noise can be 'white' (default), 'brown' or 'pink'.",
            },
        ],
        fields: [],
        methods: [
            {
                name: "setType()",
                description: "Set type of noise to 'white', 'pink' or 'brown'. White is the default.",
            },
        ],
    },
    {
        element: "p5.Amplitude",
        insert: "new p5.Amplitude()",
        code: "new p5.Amplitude([smoothing])",
        description: "Amplitude measures volume between 0.0 and 1.0. Listens to all p5sound by default, or use setInput() to listen to a specific sound source. Accepts an optional smoothing value, which defaults to 0.",
        parameters: [
            {
                name: "smoothing: Number",
                description: "between 0.0 and .999 to smooth amplitude readings (defaults to 0) (Optional)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "setInput()",
                description: "Connects to the p5sound instance (main output) by default. Optionally, you can pass in a specific source (i.e. a soundfile).",
            },
            {
                name: "getLevel()",
                description: "Returns a single Amplitude reading at the moment it is called. For continuous readings, run in the draw loop.",
            },
            {
                name: "toggleNormalize()",
                description: "Determines whether the results of Amplitude.process() will be Normalized. To normalize, Amplitude finds the difference the loudest reading it has processed and the maximum amplitude of 1.0.",
            },
            {
                name: "smooth()",
                description: "Smooth Amplitude analysis by averaging with the last analysis frame. Off by default.",
            },
        ],
    },
    {
        element: "p5.Oscillator",
        insert: "new p5.Oscillator()",
        code: "new p5.Oscillator([freq], [type])",
        description: "Creates a signal that oscillates between -1.0 and 1.0. By default, the oscillation takes the form of a sinusoidal shape ('sine'). Additional types include 'triangle', 'sawtooth' and 'square'. The frequency defaults to 440 oscillations per second (440Hz, equal to the pitch of an 'A' note).",
        parameters: [
            {
                name: "freq: Number",
                description: "frequency defaults to 440Hz (Optional)",
            },
            {
                name: "type: String",
                description: "type of oscillator. Options: 'sine' (default), 'triangle', 'sawtooth', 'square' (Optional)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "start()",
                description: "Start an oscillator. Starting an oscillator on a user gesture will enable audio in browsers that have a strict autoplay policy, including Chrome and most mobile devices.",
            },
            {
                name: "stop()",
                description: "Stop an oscillator. Accepts an optional parameter to determine how long (in seconds from now) until the oscillator stops.",
            },
            {
                name: "amp()",
                description: "Set the amplitude between 0 and 1.0. Or, pass in an object such as an oscillator to modulate amplitude with an audio signal.",
            },
            {
                name: "getAmp()",
                description: "Returns the value of output gain",
            },
            {
                name: "freq()",
                description: "Set frequency of an oscillator to a value. Or, pass in an object such as an oscillator to modulate the frequency with an audio signal.",
            },
            {
                name: "getFreq()",
                description: " Returns the value of frequency of oscillator",
            },
            {
                name: "setType()",
                description: "Set type to 'sine', 'triangle', 'sawtooth' or 'square'.",
            },
            {
                name: "getType()",
                description: "Returns current type of oscillator eg. 'sine', 'triangle', 'sawtooth' or 'square'.",
            },
            {
                name: "connect()",
                description: "Connect to a p5.sound / Web Audio object.",
            },
            {
                name: "disconnect()",
                description: "Disconnect all outputs",
            },
            {
                name: "pan()",
                description: "Pan between Left (-1) and Right (1)",
            },
            {
                name: "getPan()",
                description: "Returns the current value of panPosition , between Left (-1) and Right (1)",
            },
            {
                name: "phase()",
                description: "Set the phase of an oscillator between 0.0 and 1.0. In this implementation, phase is a delay time based on the oscillator's current frequency.",
            },
            {
                name: "add()",
                description: "Add a value to the p5.Oscillator's output amplitude, and return the oscillator. Calling this method again will override the initial add() with a new value.",
            },
            {
                name: "mult()",
                description: "Multiply the p5.Oscillator's output amplitude by a fixed value (i.e. turn it up!). Calling this method again will override the initial mult() with a new value.",
            },
            {
                name: "scale()",
                description: "Scale this oscillator's amplitude values to a given range, and return the oscillator. Calling this method again will override the initial scale() with new values.",
            },
        ],
    },
    {
        element: "p5.FFT",
        insert: "new p5.FFT()",
        code: "new p5.FFT([smoothing], [bins])",
        description: "FFT (Fast Fourier Transform) is an analysis algorithm that isolates individual audio frequencies within a waveform.",
        parameters: [
            {
                name: "smoothing: Number",
                description: "Smooth results of Freq Spectrum. 0.0 < smoothing < 1.0. Defaults to 0.8. (Optional)",
            },
            {
                name: "bins: Number",
                description: "Length of resulting array. Must be a power of two between 16 and 1024. Defaults to 1024. (Optional)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "setInput()",
                description: "Set the input source for the FFT analysis. If no source is provided, FFT will analyze all sound in the sketch.",
            },
            {
                name: "waveform()",
                description: " Returns an array of amplitude values (between -1.0 and +1.0) that represent a snapshot of amplitude readings in a single buffer.",
            },
            {
                name: "analyze()",
                description: "Returns an array of amplitude values (between 0 and 255) across the frequency spectrum. Length is equal to FFT bins (1024 by default).",
            },
            {
                name: "getEnergy()",
                description: "Returns the amount of energy (volume) at a specific frequency, or the average amount of energy between two frequencies. ",
            },
            {
                name: "getCentroid()",
                description: "Returns the spectral centroid of the input signal.",
            },
            {
                name: "smooth()",
                description: "Smooth FFT analysis by averaging with the last analysis frame.",
            },
            {
                name: "linAverages()",
                description: "Returns an array of average amplitude values for a given number of frequency bands split equally. N defaults to 16. ",
            },
            {
                name: "logAverages()",
                description: "Returns an array of average amplitude values of the spectrum, for a given set of Octave Bands",
            },
            {
                name: "getOctaveBands()",
                description: "Calculates and Returns the 1/N Octave Bands N defaults to 3 and minimum central frequency to 15.625Hz.",
            },
        ],
    },
    {
        element: "p5.AudioIn",
        insert: "new p5.AudioIn()",
        code: "new p5.AudioIn([errorCallback])",
        description: "Get audio from an input, i.e. your computer's microphone. Turn the mic on/off with the start() and stop() methods. When the mic is on, its volume can be measured with getLevel or by connecting an FFT object.",
        parameters: [
            {
                name: "errorCallback: function",
                description: "A function to call if there is an error accessing the AudioIn. For example, Safari and iOS devices do not currently allow microphone access. (Optional)",
            },
        ],
        fields: [
            {
                name: "input",
                description: "",
            },
            {
                name: "output",
                description: "",
            },
            {
                name: "stream",
                description: "",
            },
            {
                name: "mediaStream",
                description: "",
            },
            {
                name: "currentSource",
                description: "",
            },
            {
                name: "enabled",
                description: "Client must allow browser to access their microphone / audioin source. Default: false. Will become true when the client enables access.",
            },
            {
                name: "amplitude",
                description: "Input amplitude, connect to it by default but not to master out",
            },
        ],
        methods: [
            {
                name: "start()",
                description: "Start processing audio input. This enables the use of other AudioIn methods like getLevel(). Note that by default, AudioIn is not connected to p5.sound's output. So you won't hear anything unless you use the connect() method.",
            },
            {
                name: "stop()",
                description: "Turn the AudioIn off. If the AudioIn is stopped, it cannot getLevel(). If re-starting, the user may be prompted for permission access.",
            },
            {
                name: "connect()",
                description: "Connect to an audio unit. If no parameter is provided, will connect to the main output (i.e. your speakers).",
            },
            {
                name: "disconnect()",
                description: "Disconnect the AudioIn from all audio units. For example, if connect() had been called, disconnect() will stop sending signal to your speakers.",
            },
            {
                name: "getLevel()",
                description: "Read the Amplitude (volume level) of an AudioIn. The AudioIn class contains its own instance of the Amplitude class to help make it easy to get a microphone's volume level.",
            },
            {
                name: "amp()",
                description: "Set amplitude (volume) of a mic input between 0 and 1.0.",
            },
            {
                name: "getSources()",
                description: "Returns a list of available input sources. This is a wrapper for MediaDevices.enumerateDevices() - Web APIs | MDN and it returns a Promise.",
            },
            {
                name: "setSource()",
                description: "Set the input source. Accepts a number representing a position in the array returned by getSources().",
            },
        ],
    },
    {
        element: "p5.SoundFile",
        insert: "new p5.SoundFile(${1:path})",
        code: "new p5.SoundFile(path, [successCallback], [errorCallback], [whileLoadingCallback])",
        description: "SoundFile object with a path to a file. The p5.SoundFile may not be available immediately because it loads the file information asynchronously. To do something with the sound as soon as it loads pass the name of a function as the second parameter.",
        parameters: [
            {
                name: "path: String|Array",
                description: "path to a sound file (String). Optionally, you may include multiple file formats in an array. Alternately, accepts an object from the HTML5 File API, or a p5.File.",
            },
            {
                name: "successCallback: function",
                description: "Name of a function to call once file loads (Optional)",
            },
            {
                name: "errorCallback: function",
                description: "Name of a function to call if file fails to load. This function will receive an error or XMLHttpRequest object with information about what went wrong. (Optional)",
            },
            {
                name: "whileLoadingCallback: function",
                description: "Name of a function to call while file is loading. That function will receive progress of the request to load the sound file (between 0 and 1) as its first parameter. This progress does not account for the additional time needed to decode the audio data. (Optional)",
            },
        ],
        fields: [],
        methods: [
            {
                name: "isLoaded()",
                description: "Returns true if the sound file finished loading successfully.",
            },
            {
                name: "play()",
                description: "Play the p5.SoundFile",
            },
            {
                name: "playMode()",
                description: "p5.SoundFile has two play modes: restart and sustain. Play Mode determines what happens to a p5.SoundFile if it is triggered while in the middle of playback. ",
            },
            {
                name: "pause()",
                description: "Pauses a file that is currently playing. If the file is not playing, then nothing will happen. After pausing, .play() will resume from the paused position.",
            },
            {
                name: "loop()",
                description: "Loop the p5.SoundFile. Accepts optional parameters to set the playback rate, playback volume, loopStart, loopEnd.",
            },
            {
                name: "setLoop()",
                description: "Set a p5.SoundFile's looping flag to true or false. If the sound is currently playing, this change will take effect when it reaches the end of the current playback.",
            },
            {
                name: "isLooping()",
                description: "Returns 'true' if a p5.SoundFile is currently looping and playing, 'false' if not.",
            },
            {
                name: "isPlaying()",
                description: "Returns true if a p5.SoundFile is playing, false if not (i.e. paused or stopped)",
            },
            {
                name: "isPaused()",
                description: "Returns true if a p5.SoundFile is paused, false if not (i.e. playing or stopped).",
            },
            {
                name: "stop()",
                description: "Stop soundfile playback.",
            },
            {
                name: "pan()",
                description: " Set the stereo panning of a p5.sound object to a floating point number between -1.0 (left) and 1.0 (right). Default is 0.0 (center).",
            },
            {
                name: "getPan()",
                description: "Returns the current stereo pan position (-1.0 to 1.0)",
            },
            {
                name: "rate()",
                description: "Set the playback rate of a sound file. Will change the speed and the pitch. Values less than zero will reverse the audio buffer.",
            },
            {
                name: "setVolume()",
                description: "Multiply the output volume (amplitude) of a sound file between 0.0 (silence) and 1.0 (full volume). 1.0 is the maximum amplitude of a digital sound, so multiplying by greater than 1.0 may cause digital distortion. To fade, provide a rampTime parameter.",
            },
            {
                name: "duration()",
                description: "Returns the duration of a sound file in seconds.",
            },
            {
                name: "currentTime()",
                description: "Return the current position of the p5.SoundFile playhead, in seconds. Time is relative to the normal buffer direction, so if reverseBuffer has been called, currentTime will count backwards.",
            },
            {
                name: "jump()",
                description: "Move the playhead of a soundfile that is currently playing to a new position and a new duration, in seconds. ",
            },
            {
                name: "channels()",
                description: "Return the number of channels in a sound file. For example, Mono = 1, Stereo = 2.",
            },
            {
                name: "sampleRate()",
                description: "Return the sample rate of the sound file.",
            },
            {
                name: "frames()",
                description: "Return the number of samples in a sound file. Equal to sampleRate * duration.",
            },
            {
                name: "getPeaks()",
                description: "Returns an array of amplitude peaks in a p5.SoundFile that can be used to draw a static waveform. Scans through the p5.SoundFile's audio buffer to find the greatest amplitudes.",
            },
            {
                name: "reverseBuffer()",
                description: "Reverses the p5.SoundFile's buffer source. Playback must be handled separately.",
            },
            {
                name: "onended()",
                description: "Schedule an event to be called when the soundfile reaches the end of a buffer.",
            },
            {
                name: "connect()",
                description: "Connects the output of a p5sound object to input of another p5.sound object. For example, you may connect a p5.SoundFile to an FFT or an Effect. ",
            },
            {
                name: "disconnect()",
                description: "Disconnects the output of this p5sound object.",
            },
            {
                name: "setPath()",
                description: "Reset the source for this SoundFile to a new path (URL).",
            },
            {
                name: "setBuffer()",
                description: "Replace the current Audio Buffer with a new Buffer.",
            },
            {
                name: "addCue()",
                description: "Schedule events to trigger every time a MediaElement (audio/video) reaches a playback cue point. Accepts a callback function, a time (in seconds) at which to trigger the callback, and an optional parameter for the callback. ",
            },
            {
                name: "removeCue()",
                description: "Remove a callback based on its ID. The ID is returned by the addCue method.",
            },
            {
                name: "clearCues()",
                description: "Remove all of the callbacks that had originally been scheduled via the addCue method.",
            },
            {
                name: "save()",
                description: "Save a p5.SoundFile as a .wav file. The browser will prompt the user to download the file to their device.",
            },
            {
                name: "getBlob()",
                description: "This method is useful for sending a SoundFile to a server. It returns the .wav-encoded audio data as a Blob. ",
            },
        ],
    }
];
//# sourceMappingURL=classes.js.map