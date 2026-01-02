def localFrist():
    return False

#--------------------------------------------------New---------------------------------------------------------------------
INNERTUBE_CLIENTS = {
    'web': {
        'INNERTUBE_API_KEY': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'WEB',
                'clientVersion': '2.20220801.00.00',
            }
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 1
    },
    'web_embedded': {
        'INNERTUBE_API_KEY': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'WEB_EMBEDDED_PLAYER',
                'clientVersion': '1.20220731.00.00',
            },
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 56
    },
    'web_music': {
        'INNERTUBE_API_KEY': 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30',
        'INNERTUBE_HOST': 'music.youtube.com',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'WEB_REMIX',
                'clientVersion': '1.20220727.01.00',
            }
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 67,
    },
    'web_creator': {
        'INNERTUBE_API_KEY': 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'WEB_CREATOR',
                'clientVersion': '1.20220726.00.00',
            }
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 62,
    },
    'android': {
        'INNERTUBE_API_KEY': 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'ANDROID',
                'clientVersion': '18.11.34',
                'androidSdkVersion': 30,
                'userAgent': 'com.google.android.youtube/18.11.34 (Linux; U; Android 11) gzip'
            }
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 3,
        'REQUIRE_JS_PLAYER': False
    },
    'android_embedded': {
        'INNERTUBE_API_KEY': 'AIzaSyCjc_pVEDi4qsv5MtC2dMXzpIaDoRFLsxw',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'ANDROID_EMBEDDED_PLAYER',
                'clientVersion': '18.11.34',
                'androidSdkVersion': 30,
                'userAgent': 'com.google.android.youtube/18.11.34 (Linux; U; Android 11) gzip'
            },
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 55,
        'REQUIRE_JS_PLAYER': False
    },
    'android_music': {
        'INNERTUBE_API_KEY': 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'ANDROID_MUSIC',
                'clientVersion': '5.16.51',
                'androidSdkVersion': 30,
                'userAgent': 'com.google.android.apps.youtube.music/5.16.51 (Linux; U; Android 11) gzip'
            }
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 21,
        'REQUIRE_JS_PLAYER': False
    },
    'android_creator': {
        'INNERTUBE_API_KEY': 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'ANDROID_CREATOR',
                'clientVersion': '22.30.100',
                'androidSdkVersion': 30,
                'userAgent': 'com.google.android.apps.youtube.creator/22.30.100 (Linux; U; Android 11) gzip'
            },
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 14,
        'REQUIRE_JS_PLAYER': False
    },
    # iOS clients have HLS live streams. Setting device model to get 60fps formats.
    # See: https://github.com/TeamNewPipe/NewPipeExtractor/issues/680#issuecomment-1002724558
    'ios': {
        'INNERTUBE_API_KEY': 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'IOS',
                'clientVersion': '18.11.34',
                'deviceModel': 'iPhone14,3',
                'userAgent': 'com.google.ios.youtube/18.11.34 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)'
            }
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 5,
        'REQUIRE_JS_PLAYER': False
    },
    'ios_embedded': {
         'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'IOS_MESSAGES_EXTENSION',
                'clientVersion': '18.11.34',
                'deviceModel': 'iPhone14,3',
                'userAgent': 'com.google.ios.youtube/18.11.34 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)'
            },
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 66,
        'REQUIRE_JS_PLAYER': False
    },
    'ios_music': {
        'INNERTUBE_API_KEY': 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'IOS_MUSIC',
                'clientVersion': '5.21',
                'deviceModel': 'iPhone14,3',
                'userAgent': 'com.google.ios.youtubemusic/5.21 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)'
            },
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 26,
        'REQUIRE_JS_PLAYER': False
    },
    'ios_creator': {
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'IOS_CREATOR',
                'clientVersion': '22.33.101',
                'deviceModel': 'iPhone14,3',
                'userAgent': 'com.google.ios.ytcreator/22.33.101 (iPhone14,3; U; CPU iOS 15_6 like Mac OS X)'
            },
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 15,
        'REQUIRE_JS_PLAYER': False
    },
    # mweb has 'ultralow' formats
    # See: https://github.com/yt-dlp/yt-dlp/pull/557
    'mweb': {
        'INNERTUBE_API_KEY': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'MWEB',
                'clientVersion': '2.20220801.00.00',
            }
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 2
    },
    # This client can access age restricted videos (unless the uploader has disabled the 'allow embedding' option)
    # See: https://github.com/zerodytrash/YouTube-Internal-Clients
    'tv_embedded': {
        'INNERTUBE_API_KEY': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'INNERTUBE_CONTEXT': {
            'client': {
                'clientName': 'TVHTML5_SIMPLY_EMBEDDED_PLAYER',
                'clientVersion': '2.0',
            },
        },
        'INNERTUBE_CONTEXT_CLIENT_NAME': 85
    },
}
def _split_innertube_client(client_name):
    variant, *base = client_name.rsplit('.', 1)
    if base:
        return variant, base[0], variant
    base, *variant = client_name.split('_', 1)
    return client_name, base, variant[0] if variant else None


def js_to_json(code, vars={}, *, strict=False):
    import re
    import json    
    # vars is a dict of var, val pairs to substitute
    STRING_QUOTES = '\'"`'
    STRING_RE = '|'.join(rf'{q}(?:\\.|[^\\{q}])*{q}' for q in STRING_QUOTES)
    COMMENT_RE = r'/\*(?:(?!\*/).)*?\*/|//[^\n]*\n'
    SKIP_RE = fr'\s*(?:{COMMENT_RE})?\s*'
    INTEGER_TABLE = (
        (fr'(?s)^(0[xX][0-9a-fA-F]+){SKIP_RE}:?$', 16),
        (fr'(?s)^(0+[0-7]+){SKIP_RE}:?$', 8),
    )

    def process_escape(match):
        JSON_PASSTHROUGH_ESCAPES = R'"\bfnrtu'
        escape = match.group(1) or match.group(2)

        return (Rf'\{escape}' if escape in JSON_PASSTHROUGH_ESCAPES
                else R'\u00' if escape == 'x'
                else '' if escape == '\n'
                else escape)

    def template_substitute(match):
        evaluated = js_to_json(match.group(1), vars, strict=strict)
        if evaluated[0] == '"':
            return json.loads(evaluated)
        return evaluated

    def fix_kv(m):
        v = m.group(0)
        if v in ('true', 'false', 'null'):
            return v
        elif v in ('undefined', 'void 0'):
            return 'null'
        elif v.startswith('/*') or v.startswith('//') or v.startswith('!') or v == ',':
            return ''

        if v[0] in STRING_QUOTES:
            v = re.sub(r'(?s)\${([^}]+)}', template_substitute, v[1:-1]) if v[0] == '`' else v[1:-1]
            escaped = re.sub(r'(?s)(")|\\(.)', process_escape, v)
            return f'"{escaped}"'

        for regex, base in INTEGER_TABLE:
            im = re.match(regex, v)
            if im:
                i = int(im.group(1), base)
                return f'"{i}":' if v.endswith(':') else str(i)

        if v in vars:
            try:
                if not strict:
                    json.loads(vars[v])
            except json.JSONDecodeError:
                return json.dumps(vars[v])
            else:
                return vars[v]

        if not strict:
            return f'"{v}"'

        raise ValueError(f'Unknown value: {v}')

    def create_map(mobj):
        return json.dumps(dict(json.loads(js_to_json(mobj.group(1) or '[]', vars=vars))))

    code = re.sub(r'(?:new\s+)?Array\((.*?)\)', r'[\g<1>]', code)
    code = re.sub(r'new Map\((\[.*?\])?\)', create_map, code)
    if not strict:
        code = re.sub(rf'new Date\(({STRING_RE})\)', r'\g<1>', code)
        code = re.sub(r'new \w+\((.*?)\)', lambda m: json.dumps(m.group(0)), code)
        code = re.sub(r'parseInt\([^\d]+(\d+)[^\d]+\)', r'\1', code)
        code = re.sub(r'\(function\([^)]*\)\s*\{[^}]*\}\s*\)\s*\(\s*(["\'][^)]*["\'])\s*\)', r'\1', code)

    return re.sub(rf'''(?sx)
        {STRING_RE}|
        {COMMENT_RE}|,(?={SKIP_RE}[\]}}])|
        void\s0|(?:(?<![0-9])[eE]|[a-df-zA-DF-Z_$])[.a-zA-Z_$0-9]*|
        \b(?:0[xX][0-9a-fA-F]+|0+[0-7]+)(?:{SKIP_RE}:)?|
        [0-9]+(?={SKIP_RE}:)|
        !+
        ''', fix_kv, code)

def CreateExtractor(BaseCLS,
    try_get,
    clean_html,
    str_to_int,
    smuggle_url,
    int_or_none,
    unescapeHTML,
    mimetype2ext,
    parse_codecs,
    float_or_none,
    remove_quotes,
    unsmuggle_url,
    ExtractorError,
    compat_parse_qs,
    parse_duration,
    unified_strdate,
    get_element_by_id,
    compat_urllib_parse_unquote,
    compat_urllib_parse_urlparse,
    compat_urllib_parse_urlencode,
    compat_urllib_parse_unquote_plus,     
    compat_str):
    print('Youtube CoreVersion:[%s]' % '2024060601')
    import re
    import json
    import os
    
    import math
    def CreateJSInterpreter(jsCode):
        import operator
        import re
        import json
        
        _OPERATORS = [
            ('|', operator.or_),
            ('^', operator.xor),
            ('&', operator.and_),
            ('>>', operator.rshift),
            ('<<', operator.lshift),
            ('-', operator.sub),
            ('+', operator.add),
            ('%', operator.mod),
            ('/', operator.truediv),
            ('*', operator.mul),
        ]
        _ASSIGN_OPERATORS = [(op + '=', opfunc) for op, opfunc in _OPERATORS]
        _ASSIGN_OPERATORS.append(('=', lambda cur, right: right))
        _NAME_RE = r'[a-zA-Z_$][a-zA-Z_$0-9]*'
        class JSInterpreter(object):
            def __init__(self, code, objects=None):
                if objects is None:
                    objects = {}
                self.code = code
                self._functions = {}
                self._objects = objects
            def interpret_statement(self, stmt, local_vars, allow_recursion=100):
                if allow_recursion < 0:
                    raise ExtractorError('Recursion limit reached')
                should_abort = False
                stmt = stmt.lstrip()
                stmt_m = re.match(r'var\s', stmt)
                if stmt_m:
                    expr = stmt[len(stmt_m.group(0)):]
                else:
                    return_m = re.match(r'return(?:\s+|$)', stmt)
                    if return_m:
                        expr = stmt[len(return_m.group(0)):]
                        should_abort = True
                    else:
                        # Try interpreting it as an expression
                        expr = stmt
                v = self.interpret_expression(expr, local_vars, allow_recursion)
                return v, should_abort
            def interpret_expression(self, expr, local_vars, allow_recursion):
                expr = expr.strip()
                if expr == '':  # Empty expression
                    return None
                if expr.startswith('('):
                    parens_count = 0
                    for m in re.finditer(r'[()]', expr):
                        if m.group(0) == '(':
                            parens_count += 1
                        else:
                            parens_count -= 1
                            if parens_count == 0:
                                sub_expr = expr[1:m.start()]
                                sub_result = self.interpret_expression(
                                    sub_expr, local_vars, allow_recursion)
                                remaining_expr = expr[m.end():].strip()
                                if not remaining_expr:
                                    return sub_result
                                else:
                                    expr = json.dumps(sub_result) + remaining_expr
                                break
                    else:
                        raise ExtractorError('Premature end of parens in %r' % expr)
                for op, opfunc in _ASSIGN_OPERATORS:
                    m = re.match(r'''(?x)
                        (?P<out>%s)(?:\[(?P<index>[^\]]+?)\])?
                        \s*%s
                        (?P<expr>.*)$''' % (_NAME_RE, re.escape(op)), expr)
                    if not m:
                        continue
                    right_val = self.interpret_expression(
                        m.group('expr'), local_vars, allow_recursion - 1)
                    if m.groupdict().get('index'):
                        lvar = local_vars[m.group('out')]
                        idx = self.interpret_expression(
                            m.group('index'), local_vars, allow_recursion)
                        assert isinstance(idx, int)
                        cur = lvar[idx]
                        val = opfunc(cur, right_val)
                        lvar[idx] = val
                        return val
                    else:
                        cur = local_vars.get(m.group('out'))
                        val = opfunc(cur, right_val)
                        local_vars[m.group('out')] = val
                        return val
                if expr.isdigit():
                    return int(expr)
                var_m = re.match(
                    r'(?!if|return|true|false)(?P<name>%s)$' % _NAME_RE,
                    expr)
                if var_m:
                    return local_vars[var_m.group('name')]
                try:
                    return json.loads(expr)
                except ValueError:
                    pass
                m = re.match(
                    r'(?P<in>%s)\[(?P<idx>.+)\]$' % _NAME_RE, expr)
                if m:
                    val = local_vars[m.group('in')]
                    idx = self.interpret_expression(
                        m.group('idx'), local_vars, allow_recursion - 1)
                    return val[idx]
                m = re.match(
                    r'(?P<var>%s)(?:\.(?P<member>[^(]+)|\[(?P<member2>[^]]+)\])\s*(?:\(+(?P<args>[^()]*)\))?$' % _NAME_RE,
                            expr)
                if m:
                    variable = m.group('var')
                    member = remove_quotes(m.group('member') or m.group('member2'))
                    arg_str = m.group('args')
                    if variable in local_vars:
                        obj = local_vars[variable]
                    else:
                        if variable not in self._objects:
                            self._objects[variable] = self.extract_object(variable)
                        obj = self._objects[variable]
                    if arg_str is None:
                        # Member access
                        if member == 'length':
                            return len(obj)
                        return obj[member]
                    assert expr.endswith(')')
                    # Function call
                    if arg_str == '':
                        argvals = tuple()
                    else:
                        argvals = tuple([
                            self.interpret_expression(v, local_vars, allow_recursion)
                            for v in arg_str.split(',')])
                    if member == 'split':
                        assert argvals == ('',)
                        return list(obj)
                    if member == 'join':
                        assert len(argvals) == 1
                        return argvals[0].join(obj)
                    if member == 'reverse':
                        assert len(argvals) == 0
                        obj.reverse()
                        return obj
                    if member == 'slice':
                        assert len(argvals) == 1
                        return obj[argvals[0]:]
                    if member == 'splice':
                        assert isinstance(obj, list)
                        index, howMany = argvals
                        res = []
                        for i in range(index, min(index + howMany, len(obj))):
                            res.append(obj.pop(index))
                        return res
                    return obj[member](argvals)
                for op, opfunc in _OPERATORS:
                    m = re.match(r'(?P<x>.+?)%s(?P<y>.+)' % re.escape(op), expr)
                    if not m:
                        continue
                    x, abort = self.interpret_statement(
                        m.group('x'), local_vars, allow_recursion - 1)
                    if abort:
                        raise ExtractorError(
                            'Premature left-side return of %s in %r' % (op, expr))
                    y, abort = self.interpret_statement(
                        m.group('y'), local_vars, allow_recursion - 1)
                    if abort:
                        raise ExtractorError(
                            'Premature right-side return of %s in %r' % (op, expr))
                    return opfunc(x, y)
                m = re.match(
                    r'^(?P<func>%s)\((?P<args>[a-zA-Z0-9_$,]*)\)$' % _NAME_RE, expr)
                if m:
                    fname = m.group('func')
                    argvals = tuple([
                        int(v) if v.isdigit() else local_vars[v]
                        for v in m.group('args').split(',')]) if len(m.group('args')) > 0 else tuple()
                    if fname not in self._functions:
                        self._functions[fname] = self.extract_function(fname)
                    return self._functions[fname](argvals)
                raise ExtractorError('Unsupported JS expression %r' % expr)
            
            def extract_object(self, objname):
                _FUNC_NAME_RE = r'''(?:[a-zA-Z$0-9]+|"[a-zA-Z$0-9]+"|'[a-zA-Z$0-9]+')'''
                obj = {}
                obj_m = re.search(
                    r'''(?x)
                        (?<!this\.)%s\s*=\s*{\s*
                        (?P<fields>(%s\s*:\s*function\s*\(.*?\)\s*{.*?}(?:,\s*)?)*)
                        }\s*;
            ''' % (re.escape(objname), _FUNC_NAME_RE),
                    self.code)
                fields = obj_m.group('fields')
                # Currently, it only supports function definitions
                fields_m = re.finditer(
                    r'''(?x)
                        (?P<key>%s)\s*:\s*function\s*\((?P<args>[a-z,]+)\){(?P<code>[^}]+)}
                     ''' % _FUNC_NAME_RE,
                    fields)
                for f in fields_m:
                    argnames = f.group('args').split(',')
                    obj[remove_quotes(f.group('key'))] = self.build_function(argnames, f.group('code'))
                return obj
            
            def extract_function(self, funcname):
                func_m = re.search(
                    r'''(?x)
                        (?:function\s+%s|[{;,]\s*%s\s*=\s*function|var\s+%s\s*=\s*function)\s*
                        \((?P<args>[^)]*)\)\s*
                        \{(?P<code>[^}]+)\}''' % (
                        re.escape(funcname), re.escape(funcname), re.escape(funcname)),
                    self.code)
                if func_m is None:
                    raise ExtractorError('Could not find JS function %r' % funcname)
                argnames = func_m.group('args').split(',')
                return self.build_function(argnames, func_m.group('code'))     

            
            def call_function(self, funcname, *args):
                f = self.extract_function(funcname)
                return f(args)
            
            def build_function(self, argnames, code):
                def resf(args):
                    local_vars = dict(zip(argnames, args))
                    for stmt in code.split(';'):
                        res, abort = self.interpret_statement(stmt, local_vars)
                        if abort:
                            break
                    return res
                return resf
            
        return JSInterpreter(jsCode)
    
    def CreateJSInterpreterEx(jsCode):
        import operator
        import contextlib
        import functools
        import collections
        import datetime as dt
        import calendar
        import email.header
        import email.utils
        import itertools

        DATE_FORMATS = (
            '%d %B %Y',
            '%d %b %Y',
            '%B %d %Y',
            '%B %dst %Y',
            '%B %dnd %Y',
            '%B %drd %Y',
            '%B %dth %Y',
            '%b %d %Y',
            '%b %dst %Y',
            '%b %dnd %Y',
            '%b %drd %Y',
            '%b %dth %Y',
            '%b %dst %Y %I:%M',
            '%b %dnd %Y %I:%M',
            '%b %drd %Y %I:%M',
            '%b %dth %Y %I:%M',
            '%Y %m %d',
            '%Y-%m-%d',
            '%Y.%m.%d.',
            '%Y/%m/%d',
            '%Y/%m/%d %H:%M',
            '%Y/%m/%d %H:%M:%S',
            '%Y%m%d%H%M',
            '%Y%m%d%H%M%S',
            '%Y%m%d',
            '%Y-%m-%d %H:%M',
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d %H:%M:%S.%f',
            '%Y-%m-%d %H:%M:%S:%f',
            '%d.%m.%Y %H:%M',
            '%d.%m.%Y %H.%M',
            '%Y-%m-%dT%H:%M:%SZ',
            '%Y-%m-%dT%H:%M:%S.%fZ',
            '%Y-%m-%dT%H:%M:%S.%f0Z',
            '%Y-%m-%dT%H:%M:%S',
            '%Y-%m-%dT%H:%M:%S.%f',
            '%Y-%m-%dT%H:%M',
            '%b %d %Y at %H:%M',
            '%b %d %Y at %H:%M:%S',
            '%B %d %Y at %H:%M',
            '%B %d %Y at %H:%M:%S',
            '%H:%M %d-%b-%Y',
        )
        DATE_FORMATS_DAY_FIRST = list(DATE_FORMATS)
        DATE_FORMATS_DAY_FIRST.extend([
            '%d-%m-%Y',
            '%d.%m.%Y',
            '%d.%m.%y',
            '%d/%m/%Y',
            '%d/%m/%y',
            '%d/%m/%Y %H:%M:%S',
            '%d-%m-%Y %H:%M',
            '%H:%M %d/%m/%Y',
        ])        
        DATE_FORMATS_MONTH_FIRST = list(DATE_FORMATS)
        DATE_FORMATS_MONTH_FIRST.extend([
            '%m-%d-%Y',
            '%m.%d.%Y',
            '%m/%d/%Y',
            '%m/%d/%y',
            '%m/%d/%Y %H:%M:%S',
        ])

        def date_formats(day_first=True):
            return DATE_FORMATS_DAY_FIRST if day_first else DATE_FORMATS_MONTH_FIRST        

        def extract_timezone(date_str, default=None):
            TIMEZONE_NAMES = {
                'UT': 0, 'UTC': 0, 'GMT': 0, 'Z': 0,
                'AST': -4, 'ADT': -3,  # Atlantic (used in Canada)
                'EST': -5, 'EDT': -4,  # Eastern
                'CST': -6, 'CDT': -5,  # Central
                'MST': -7, 'MDT': -6,  # Mountain
                'PST': -8, 'PDT': -7   # Pacific
            }
            m = re.search(
                r'''(?x)
                    ^.{8,}?                                              # >=8 char non-TZ prefix, if present
                    (?P<tz>Z|                                            # just the UTC Z, or
                        (?:(?<=.\b\d{4}|\b\d{2}:\d\d)|                   # preceded by 4 digits or hh:mm or
                        (?<!.\b[a-zA-Z]{3}|[a-zA-Z]{4}|..\b\d\d))     # not preceded by 3 alpha word or >= 4 alpha or 2 digits
                        [ ]?                                          # optional space
                        (?P<sign>\+|-)                                   # +/-
                        (?P<hours>[0-9]{2}):?(?P<minutes>[0-9]{2})       # hh[:]mm
                    $)
                ''', date_str)
            timezone = None

            if not m:
                m = re.search(r'\d{1,2}:\d{1,2}(?:\.\d+)?(?P<tz>\s*[A-Z]+)$', date_str)
                timezone = TIMEZONE_NAMES.get(m and m.group('tz').strip())
                if timezone is not None:
                    date_str = date_str[:-len(m.group('tz'))]
                    timezone = dt.timedelta(hours=timezone)
            else:
                date_str = date_str[:-len(m.group('tz'))]
                if m.group('sign'):
                    sign = 1 if m.group('sign') == '+' else -1
                    timezone = dt.timedelta(
                        hours=sign * int(m.group('hours')),
                        minutes=sign * int(m.group('minutes')))

            if timezone is None and default is not NO_DEFAULT:
                timezone = default or dt.timedelta()

            return timezone, date_str

        class function_with_repr:
            def __init__(self, func, repr_=None):
                functools.update_wrapper(self, func)
                self.func, self.__repr = func, repr_

            def __call__(self, *args, **kwargs):
                return self.func(*args, **kwargs)

            @classmethod
            def set_repr(cls, repr_):
                return functools.partial(cls, repr_=repr_)

            def __repr__(self):
                if self.__repr:
                    return self.__repr
                return f'{self.func.__module__}.{self.func.__qualname__}'
            
        def unified_timestamp(date_str, day_first=True):
            if not isinstance(date_str, str):
                return None

            date_str = re.sub(r'\s+', ' ', re.sub(
                r'(?i)[,|]|(mon|tues?|wed(nes)?|thu(rs)?|fri|sat(ur)?)(day)?', '', date_str))

            pm_delta = 12 if re.search(r'(?i)PM', date_str) else 0
            timezone, date_str = extract_timezone(date_str)

            # Remove AM/PM + timezone
            date_str = re.sub(r'(?i)\s*(?:AM|PM)(?:\s+[A-Z]+)?', '', date_str)

            # Remove unrecognized timezones from ISO 8601 alike timestamps
            m = re.search(r'\d{1,2}:\d{1,2}(?:\.\d+)?(?P<tz>\s*[A-Z]+)$', date_str)
            if m:
                date_str = date_str[:-len(m.group('tz'))]

            # Python only supports microseconds, so remove nanoseconds
            m = re.search(r'^([0-9]{4,}-[0-9]{1,2}-[0-9]{1,2}T[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{6})[0-9]+$', date_str)
            if m:
                date_str = m.group(1)

            for expression in date_formats(day_first):
                with contextlib.suppress(ValueError):
                    dt_ = dt.datetime.strptime(date_str, expression) - timezone + dt.timedelta(hours=pm_delta)
                    return calendar.timegm(dt_.timetuple())

            timetuple = email.utils.parsedate_tz(date_str)
            if timetuple:
                return calendar.timegm(timetuple) + pm_delta * 3600 - timezone.total_seconds()            


        def truncate_string(s, left, right=0):
            assert left > 3 and right >= 0
            if s is None or len(s) <= left + right:
                return s
            return f'{s[:left - 3]}...{s[-right:] if right else ""}'

        def _js_bit_op(op):
            def zeroise(x):
                if x in (None, JS_Undefined):
                    return 0
                with contextlib.suppress(TypeError):
                    if math.isnan(x):  # NB: NaN cannot be checked by membership
                        return 0
                return x

            def wrapped(a, b):
                return op(zeroise(a), zeroise(b)) & 0xffffffff

            return wrapped


        def _js_arith_op(op):

            def wrapped(a, b):
                if JS_Undefined in (a, b):
                    return float('nan')
                return op(a or 0, b or 0)

            return wrapped


        def _js_div(a, b):
            if JS_Undefined in (a, b) or not (a or b):
                return float('nan')
            return (a or 0) / b if b else float('inf')


        def _js_mod(a, b):
            if JS_Undefined in (a, b) or not b:
                return float('nan')
            return (a or 0) % b


        def _js_exp(a, b):
            if not b:
                return 1  # even 0 ** 0 !!
            elif JS_Undefined in (a, b):
                return float('nan')
            return (a or 0) ** b


        def _js_eq_op(op):

            def wrapped(a, b):
                if {a, b} <= {None, JS_Undefined}:
                    return op(a, a)
                return op(a, b)

            return wrapped


        def _js_comp_op(op):

            def wrapped(a, b):
                if JS_Undefined in (a, b):
                    return False
                if isinstance(a, str) or isinstance(b, str):
                    return op(str(a or 0), str(b or 0))
                return op(a or 0, b or 0)

            return wrapped


        def _js_ternary(cndn, if_true=True, if_false=False):
            """Simulate JS's ternary operator (cndn?if_true:if_false)"""
            if cndn in (False, None, 0, '', JS_Undefined):
                return if_false
            with contextlib.suppress(TypeError):
                if math.isnan(cndn):  # NB: NaN cannot be checked by membership
                    return if_false
            return if_true


        # Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence
        _OPERATORS = {  # None => Defined in JSInterpreter._operator
            '?': None,
            '??': None,
            '||': None,
            '&&': None,

            '|': _js_bit_op(operator.or_),
            '^': _js_bit_op(operator.xor),
            '&': _js_bit_op(operator.and_),

            '===': operator.is_,
            '!==': operator.is_not,
            '==': _js_eq_op(operator.eq),
            '!=': _js_eq_op(operator.ne),

            '<=': _js_comp_op(operator.le),
            '>=': _js_comp_op(operator.ge),
            '<': _js_comp_op(operator.lt),
            '>': _js_comp_op(operator.gt),

            '>>': _js_bit_op(operator.rshift),
            '<<': _js_bit_op(operator.lshift),

            '+': _js_arith_op(operator.add),
            '-': _js_arith_op(operator.sub),

            '*': _js_arith_op(operator.mul),
            '%': _js_mod,
            '/': _js_div,
            '**': _js_exp,
        }

        _COMP_OPERATORS = {'===', '!==', '==', '!=', '<=', '>=', '<', '>'}

        _NAME_RE = r'[a-zA-Z_$][\w$]*'
        _MATCHING_PARENS = dict(zip(*zip('()', '{}', '[]')))
        _QUOTES = '\'"/'


        class JS_Undefined:
            pass


        class JS_Break(ExtractorError):
            def __init__(self):
                ExtractorError.__init__(self, 'Invalid break')


        class JS_Continue(ExtractorError):
            def __init__(self):
                ExtractorError.__init__(self, 'Invalid continue')


        class JS_Throw(ExtractorError):
            def __init__(self, e):
                self.error = e
                ExtractorError.__init__(self, f'Uncaught exception {e}')


        class LocalNameSpace(collections.ChainMap):
            def __setitem__(self, key, value):
                for scope in self.maps:
                    if key in scope:
                        scope[key] = value
                        return
                self.maps[0][key] = value

            def __delitem__(self, key):
                raise NotImplementedError('Deleting is not supported')


        class Debugger:
            import sys
            ENABLED = False and 'pytest' in sys.modules

            @staticmethod
            def write(*args, level=100):
                pass
                # write_string(f'[debug] JS: {"  " * (100 - level)}'
                #             f'{" ".join(truncate_string(str(x), 50, 50) for x in args)}\n')

            @classmethod
            def wrap_interpreter(cls, f):
                def interpret_statement(self, stmt, local_vars, allow_recursion, *args, **kwargs):
                    if cls.ENABLED and stmt.strip():
                        cls.write(stmt, level=allow_recursion)
                    try:
                        ret, should_ret = f(self, stmt, local_vars, allow_recursion, *args, **kwargs)
                    except Exception as e:
                        if cls.ENABLED:
                            if isinstance(e, ExtractorError):
                                e = e.orig_msg
                            cls.write('=> Raises:', e, '<-|', stmt, level=allow_recursion)
                        raise
                    if cls.ENABLED and stmt.strip():
                        if should_ret or not repr(ret) == stmt:
                            cls.write(['->', '=>'][should_ret], repr(ret), '<-|', stmt, level=allow_recursion)
                    return ret, should_ret
                return interpret_statement


        class JSInterpreter:
            __named_object_counter = 0

            _RE_FLAGS = {
                # special knowledge: Python's re flags are bitmask values, current max 128
                # invent new bitmask values well above that for literal parsing
                # TODO: new pattern class to execute matches with these flags
                'd': 1024,  # Generate indices for substring matches
                'g': 2048,  # Global search
                'i': re.I,  # Case-insensitive search
                'm': re.M,  # Multi-line search
                's': re.S,  # Allows . to match newline characters
                'u': re.U,  # Treat a pattern as a sequence of unicode code points
                'y': 4096,  # Perform a "sticky" search that matches starting at the current position in the target string
            }

            def __init__(self, code, objects=None):
                self.code, self._functions = code, {}
                self._objects = {} if objects is None else objects

            class Exception(ExtractorError):
                def __init__(self, msg, expr=None, *args, **kwargs):
                    if expr is not None:
                        msg = f'{msg.rstrip()} in: {truncate_string(expr, 50, 50)}'
                    super().__init__(msg, *args, **kwargs)

            def _named_object(self, namespace, obj):
                self.__named_object_counter += 1
                name = f'__yt_dlp_jsinterp_obj{self.__named_object_counter}'
                if callable(obj) and not isinstance(obj, function_with_repr):
                    obj = function_with_repr(obj, f'F<{self.__named_object_counter}>')
                namespace[name] = obj
                return name

            @classmethod
            def _regex_flags(cls, expr):
                flags = 0
                if not expr:
                    return flags, expr
                for idx, ch in enumerate(expr):
                    if ch not in cls._RE_FLAGS:
                        break
                    flags |= cls._RE_FLAGS[ch]
                return flags, expr[idx + 1:]

            @staticmethod
            def _separate(expr, delim=',', max_split=None):
                OP_CHARS = '+-*/%&|^=<>!,;{}:['
                if not expr:
                    return
                counters = {k: 0 for k in _MATCHING_PARENS.values()}
                start, splits, pos, delim_len = 0, 0, 0, len(delim) - 1
                in_quote, escaping, after_op, in_regex_char_group = None, False, True, False
                for idx, char in enumerate(expr):
                    if not in_quote and char in _MATCHING_PARENS:
                        counters[_MATCHING_PARENS[char]] += 1
                    elif not in_quote and char in counters:
                        # Something's wrong if we get negative, but ignore it anyway
                        if counters[char]:
                            counters[char] -= 1
                    elif not escaping:
                        if char in _QUOTES and in_quote in (char, None):
                            if in_quote or after_op or char != '/':
                                in_quote = None if in_quote and not in_regex_char_group else char
                        elif in_quote == '/' and char in '[]':
                            in_regex_char_group = char == '['
                    escaping = not escaping and in_quote and char == '\\'
                    in_unary_op = (not in_quote and not in_regex_char_group
                                and after_op not in (True, False) and char in '-+')
                    after_op = char if (not in_quote and char in OP_CHARS) else (char.isspace() and after_op)

                    if char != delim[pos] or any(counters.values()) or in_quote or in_unary_op:
                        pos = 0
                        continue
                    elif pos != delim_len:
                        pos += 1
                        continue
                    yield expr[start: idx - delim_len]
                    start, pos = idx + 1, 0
                    splits += 1
                    if max_split and splits >= max_split:
                        break
                yield expr[start:]

            @classmethod
            def _separate_at_paren(cls, expr, delim=None):
                if delim is None:
                    delim = expr and _MATCHING_PARENS[expr[0]]
                separated = list(cls._separate(expr, delim, 1))
                if len(separated) < 2:
                    raise cls.Exception(f'No terminating paren {delim}', expr)
                return separated[0][1:].strip(), separated[1].strip()

            def _operator(self, op, left_val, right_expr, expr, local_vars, allow_recursion):
                if op in ('||', '&&'):
                    if (op == '&&') ^ _js_ternary(left_val):
                        return left_val  # short circuiting
                elif op == '??':
                    if left_val not in (None, JS_Undefined):
                        return left_val
                elif op == '?':
                    right_expr = _js_ternary(left_val, *self._separate(right_expr, ':', 1))

                right_val = self.interpret_expression(right_expr, local_vars, allow_recursion)
                if not _OPERATORS.get(op):
                    return right_val

                try:
                    return _OPERATORS[op](left_val, right_val)
                except Exception as e:
                    raise self.Exception(f'Failed to evaluate {left_val!r} {op} {right_val!r}', expr, cause=e)

            def _index(self, obj, idx, allow_undefined=False):
                if idx == 'length':
                    return len(obj)
                try:
                    return obj[int(idx)] if isinstance(obj, list) else obj[idx]
                except Exception as e:
                    if allow_undefined:
                        return JS_Undefined
                    raise self.Exception(f'Cannot get index {idx}', repr(obj), cause=e)

            def _dump(self, obj, namespace):
                try:
                    return json.dumps(obj)
                except TypeError:
                    return self._named_object(namespace, obj)

            @Debugger.wrap_interpreter
            def interpret_statement(self, stmt, local_vars, allow_recursion=100):
                if allow_recursion < 0:
                    raise self.Exception('Recursion limit reached')
                allow_recursion -= 1

                should_return = False
                sub_statements = list(self._separate(stmt, ';')) or ['']
                expr = stmt = sub_statements.pop().strip()

                for sub_stmt in sub_statements:
                    ret, should_return = self.interpret_statement(sub_stmt, local_vars, allow_recursion)
                    if should_return:
                        return ret, should_return

                m = re.match(r'(?P<var>(?:var|const|let)\s)|return(?:\s+|(?=["\'])|$)|(?P<throw>throw\s+)', stmt)
                if m:
                    expr = stmt[len(m.group(0)):].strip()
                    if m.group('throw'):
                        raise JS_Throw(self.interpret_expression(expr, local_vars, allow_recursion))
                    should_return = not m.group('var')
                if not expr:
                    return None, should_return

                if expr[0] in _QUOTES:
                    inner, outer = self._separate(expr, expr[0], 1)
                    if expr[0] == '/':
                        flags, outer = self._regex_flags(outer)
                        # We don't support regex methods yet, so no point compiling it
                        inner = f'{inner}/{flags}'
                        # Avoid https://github.com/python/cpython/issues/74534
                        # inner = re.compile(inner[1:].replace('[[', r'[\['), flags=flags)
                    else:
                        inner = json.loads(js_to_json(f'{inner}{expr[0]}', strict=True))
                    if not outer:
                        return inner, should_return
                    expr = self._named_object(local_vars, inner) + outer

                if expr.startswith('new '):
                    obj = expr[4:]
                    if obj.startswith('Date('):
                        left, right = self._separate_at_paren(obj[4:])
                        date = unified_timestamp(
                            self.interpret_expression(left, local_vars, allow_recursion), False)
                        if date is None:
                            raise self.Exception(f'Failed to parse date {left!r}', expr)
                        expr = self._dump(int(date * 1000), local_vars) + right
                    else:
                        raise self.Exception(f'Unsupported object {obj}', expr)

                if expr.startswith('void '):
                    left = self.interpret_expression(expr[5:], local_vars, allow_recursion)
                    return None, should_return

                if expr.startswith('{'):
                    inner, outer = self._separate_at_paren(expr)
                    # try for object expression (Map)
                    sub_expressions = [list(self._separate(sub_expr.strip(), ':', 1)) for sub_expr in self._separate(inner)]
                    if all(len(sub_expr) == 2 for sub_expr in sub_expressions):
                        def dict_item(key, val):
                            val = self.interpret_expression(val, local_vars, allow_recursion)
                            if re.match(_NAME_RE, key):
                                return key, val
                            return self.interpret_expression(key, local_vars, allow_recursion), val

                        return dict(dict_item(k, v) for k, v in sub_expressions), should_return

                    inner, should_abort = self.interpret_statement(inner, local_vars, allow_recursion)
                    if not outer or should_abort:
                        return inner, should_abort or should_return
                    else:
                        expr = self._dump(inner, local_vars) + outer

                if expr.startswith('('):
                    inner, outer = self._separate_at_paren(expr)
                    inner, should_abort = self.interpret_statement(inner, local_vars, allow_recursion)
                    if not outer or should_abort:
                        return inner, should_abort or should_return
                    else:
                        expr = self._dump(inner, local_vars) + outer

                if expr.startswith('['):
                    inner, outer = self._separate_at_paren(expr)
                    name = self._named_object(local_vars, [
                        self.interpret_expression(item, local_vars, allow_recursion)
                        for item in self._separate(inner)])
                    expr = name + outer

                m = re.match(r'''(?x)
                        (?P<try>try)\s*\{|
                        (?P<if>if)\s*\(|
                        (?P<switch>switch)\s*\(|
                        (?P<for>for)\s*\(
                        ''', expr)
                md = m.groupdict() if m else {}
                if md.get('if'):
                    cndn, expr = self._separate_at_paren(expr[m.end() - 1:])
                    if_expr, expr = self._separate_at_paren(expr.lstrip())
                    # TODO: "else if" is not handled
                    else_expr = None
                    m = re.match(r'else\s*{', expr)
                    if m:
                        else_expr, expr = self._separate_at_paren(expr[m.end() - 1:])
                    cndn = _js_ternary(self.interpret_expression(cndn, local_vars, allow_recursion))
                    ret, should_abort = self.interpret_statement(
                        if_expr if cndn else else_expr, local_vars, allow_recursion)
                    if should_abort:
                        return ret, True

                if md.get('try'):
                    try_expr, expr = self._separate_at_paren(expr[m.end() - 1:])
                    err = None
                    try:
                        ret, should_abort = self.interpret_statement(try_expr, local_vars, allow_recursion)
                        if should_abort:
                            return ret, True
                    except Exception as e:
                        # XXX: This works for now, but makes debugging future issues very hard
                        err = e

                    pending = (None, False)
                    m = re.match(fr'catch\s*(?P<err>\(\s*{_NAME_RE}\s*\))?\{{', expr)
                    if m:
                        sub_expr, expr = self._separate_at_paren(expr[m.end() - 1:])
                        if err:
                            catch_vars = {}
                            if m.group('err'):
                                catch_vars[m.group('err')] = err.error if isinstance(err, JS_Throw) else err
                            catch_vars = local_vars.new_child(catch_vars)
                            err, pending = None, self.interpret_statement(sub_expr, catch_vars, allow_recursion)

                    m = re.match(r'finally\s*\{', expr)
                    if m:
                        sub_expr, expr = self._separate_at_paren(expr[m.end() - 1:])
                        ret, should_abort = self.interpret_statement(sub_expr, local_vars, allow_recursion)
                        if should_abort:
                            return ret, True

                    ret, should_abort = pending
                    if should_abort:
                        return ret, True

                    if err:
                        raise err

                elif md.get('for'):
                    constructor, remaining = self._separate_at_paren(expr[m.end() - 1:])
                    if remaining.startswith('{'):
                        body, expr = self._separate_at_paren(remaining)
                    else:
                        switch_m = re.match(r'switch\s*\(', remaining)  # FIXME
                        if switch_m:
                            switch_val, remaining = self._separate_at_paren(remaining[switch_m.end() - 1:])
                            body, expr = self._separate_at_paren(remaining, '}')
                            body = 'switch(%s){%s}' % (switch_val, body)
                        else:
                            body, expr = remaining, ''
                    start, cndn, increment = self._separate(constructor, ';')
                    self.interpret_expression(start, local_vars, allow_recursion)
                    while True:
                        if not _js_ternary(self.interpret_expression(cndn, local_vars, allow_recursion)):
                            break
                        try:
                            ret, should_abort = self.interpret_statement(body, local_vars, allow_recursion)
                            if should_abort:
                                return ret, True
                        except JS_Break:
                            break
                        except JS_Continue:
                            pass
                        self.interpret_expression(increment, local_vars, allow_recursion)

                elif md.get('switch'):
                    switch_val, remaining = self._separate_at_paren(expr[m.end() - 1:])
                    switch_val = self.interpret_expression(switch_val, local_vars, allow_recursion)
                    body, expr = self._separate_at_paren(remaining, '}')
                    items = body.replace('default:', 'case default:').split('case ')[1:]
                    for default in (False, True):
                        matched = False
                        for item in items:
                            case, stmt = (i.strip() for i in self._separate(item, ':', 1))
                            if default:
                                matched = matched or case == 'default'
                            elif not matched:
                                matched = (case != 'default'
                                        and switch_val == self.interpret_expression(case, local_vars, allow_recursion))
                            if not matched:
                                continue
                            try:
                                ret, should_abort = self.interpret_statement(stmt, local_vars, allow_recursion)
                                if should_abort:
                                    return ret
                            except JS_Break:
                                break
                        if matched:
                            break

                if md:
                    ret, should_abort = self.interpret_statement(expr, local_vars, allow_recursion)
                    return ret, should_abort or should_return

                # Comma separated statements
                sub_expressions = list(self._separate(expr))
                if len(sub_expressions) > 1:
                    for sub_expr in sub_expressions:
                        ret, should_abort = self.interpret_statement(sub_expr, local_vars, allow_recursion)
                        if should_abort:
                            return ret, True
                    return ret, False

                for m in re.finditer(rf'''(?x)
                        (?P<pre_sign>\+\+|--)(?P<var1>{_NAME_RE})|
                        (?P<var2>{_NAME_RE})(?P<post_sign>\+\+|--)''', expr):
                    var = m.group('var1') or m.group('var2')
                    start, end = m.span()
                    sign = m.group('pre_sign') or m.group('post_sign')
                    ret = local_vars[var]
                    local_vars[var] += 1 if sign[0] == '+' else -1
                    if m.group('pre_sign'):
                        ret = local_vars[var]
                    expr = expr[:start] + self._dump(ret, local_vars) + expr[end:]

                if not expr:
                    return None, should_return

                m = re.match(fr'''(?x)
                    (?P<assign>
                        (?P<out>{_NAME_RE})(?:\[(?P<index>[^\]]+?)\])?\s*
                        (?P<op>{"|".join(map(re.escape, set(_OPERATORS) - _COMP_OPERATORS))})?
                        =(?!=)(?P<expr>.*)$
                    )|(?P<return>
                        (?!if|return|true|false|null|undefined|NaN)(?P<name>{_NAME_RE})$
                    )|(?P<indexing>
                        (?P<in>{_NAME_RE})\[(?P<idx>.+)\]$
                    )|(?P<attribute>
                        (?P<var>{_NAME_RE})(?:(?P<nullish>\?)?\.(?P<member>[^(]+)|\[(?P<member2>[^\]]+)\])\s*
                    )|(?P<function>
                        (?P<fname>{_NAME_RE})\((?P<args>.*)\)$
                    )''', expr)
                if m and m.group('assign'):
                    left_val = local_vars.get(m.group('out'))

                    if not m.group('index'):
                        local_vars[m.group('out')] = self._operator(
                            m.group('op'), left_val, m.group('expr'), expr, local_vars, allow_recursion)
                        return local_vars[m.group('out')], should_return
                    elif left_val in (None, JS_Undefined):
                        raise self.Exception(f'Cannot index undefined variable {m.group("out")}', expr)

                    idx = self.interpret_expression(m.group('index'), local_vars, allow_recursion)
                    if not isinstance(idx, (int, float)):
                        raise self.Exception(f'List index {idx} must be integer', expr)
                    idx = int(idx)
                    left_val[idx] = self._operator(
                        m.group('op'), self._index(left_val, idx), m.group('expr'), expr, local_vars, allow_recursion)
                    return left_val[idx], should_return

                elif expr.isdigit():
                    return int(expr), should_return

                elif expr == 'break':
                    raise JS_Break()
                elif expr == 'continue':
                    raise JS_Continue()
                elif expr == 'undefined':
                    return JS_Undefined, should_return
                elif expr == 'NaN':
                    return float('NaN'), should_return

                elif m and m.group('return'):
                    return local_vars.get(m.group('name'), JS_Undefined), should_return

                with contextlib.suppress(ValueError):
                    return json.loads(js_to_json(expr, strict=True)), should_return

                if m and m.group('indexing'):
                    val = local_vars[m.group('in')]
                    idx = self.interpret_expression(m.group('idx'), local_vars, allow_recursion)
                    return self._index(val, idx), should_return

                for op in _OPERATORS:
                    separated = list(self._separate(expr, op))
                    right_expr = separated.pop()
                    while True:
                        if op in '?<>*-' and len(separated) > 1 and not separated[-1].strip():
                            separated.pop()
                        elif not (separated and op == '?' and right_expr.startswith('.')):
                            break
                        right_expr = f'{op}{right_expr}'
                        if op != '-':
                            right_expr = f'{separated.pop()}{op}{right_expr}'
                    if not separated:
                        continue
                    left_val = self.interpret_expression(op.join(separated), local_vars, allow_recursion)
                    return self._operator(op, left_val, right_expr, expr, local_vars, allow_recursion), should_return

                if m and m.group('attribute'):
                    variable, member, nullish = m.group('var', 'member', 'nullish')
                    if not member:
                        member = self.interpret_expression(m.group('member2'), local_vars, allow_recursion)
                    arg_str = expr[m.end():]
                    if arg_str.startswith('('):
                        arg_str, remaining = self._separate_at_paren(arg_str)
                    else:
                        arg_str, remaining = None, arg_str

                    def assertion(cndn, msg):
                        """ assert, but without risk of getting optimized out """
                        if not cndn:
                            raise self.Exception(f'{member} {msg}', expr)

                    def eval_method():
                        if (variable, member) == ('console', 'debug'):
                            if Debugger.ENABLED:
                                Debugger.write(self.interpret_expression(f'[{arg_str}]', local_vars, allow_recursion))
                            return

                        types = {
                            'String': str,
                            'Math': float,
                        }
                        obj = local_vars.get(variable, types.get(variable, NO_DEFAULT))
                        if obj is NO_DEFAULT:
                            if variable not in self._objects:
                                try:
                                    self._objects[variable] = self.extract_object(variable)
                                except self.Exception:
                                    if not nullish:
                                        raise
                            obj = self._objects.get(variable, JS_Undefined)

                        if nullish and obj is JS_Undefined:
                            return JS_Undefined

                        # Member access
                        if arg_str is None:
                            return self._index(obj, member, nullish)

                        # Function call
                        argvals = [
                            self.interpret_expression(v, local_vars, allow_recursion)
                            for v in self._separate(arg_str)]

                        if obj == str:
                            if member == 'fromCharCode':
                                assertion(argvals, 'takes one or more arguments')
                                return ''.join(map(chr, argvals))
                            raise self.Exception(f'Unsupported String method {member}', expr)
                        elif obj == float:
                            if member == 'pow':
                                assertion(len(argvals) == 2, 'takes two arguments')
                                return argvals[0] ** argvals[1]
                            raise self.Exception(f'Unsupported Math method {member}', expr)

                        if member == 'split':
                            assertion(argvals, 'takes one or more arguments')
                            assertion(len(argvals) == 1, 'with limit argument is not implemented')
                            return obj.split(argvals[0]) if argvals[0] else list(obj)
                        elif member == 'join':
                            assertion(isinstance(obj, list), 'must be applied on a list')
                            assertion(len(argvals) == 1, 'takes exactly one argument')
                            return argvals[0].join(obj)
                        elif member == 'reverse':
                            assertion(not argvals, 'does not take any arguments')
                            obj.reverse()
                            return obj
                        elif member == 'slice':
                            assertion(isinstance(obj, list), 'must be applied on a list')
                            assertion(len(argvals) == 1, 'takes exactly one argument')
                            return obj[argvals[0]:]
                        elif member == 'splice':
                            assertion(isinstance(obj, list), 'must be applied on a list')
                            assertion(argvals, 'takes one or more arguments')
                            index, howMany = map(int, (argvals + [len(obj)])[:2])
                            if index < 0:
                                index += len(obj)
                            add_items = argvals[2:]
                            res = []
                            for i in range(index, min(index + howMany, len(obj))):
                                res.append(obj.pop(index))
                            for i, item in enumerate(add_items):
                                obj.insert(index + i, item)
                            return res
                        elif member == 'unshift':
                            assertion(isinstance(obj, list), 'must be applied on a list')
                            assertion(argvals, 'takes one or more arguments')
                            for item in reversed(argvals):
                                obj.insert(0, item)
                            return obj
                        elif member == 'pop':
                            assertion(isinstance(obj, list), 'must be applied on a list')
                            assertion(not argvals, 'does not take any arguments')
                            if not obj:
                                return
                            return obj.pop()
                        elif member == 'push':
                            assertion(argvals, 'takes one or more arguments')
                            obj.extend(argvals)
                            return obj
                        elif member == 'forEach':
                            assertion(argvals, 'takes one or more arguments')
                            assertion(len(argvals) <= 2, 'takes at-most 2 arguments')
                            f, this = (argvals + [''])[:2]
                            return [f((item, idx, obj), {'this': this}, allow_recursion) for idx, item in enumerate(obj)]
                        elif member == 'indexOf':
                            assertion(argvals, 'takes one or more arguments')
                            assertion(len(argvals) <= 2, 'takes at-most 2 arguments')
                            idx, start = (argvals + [0])[:2]
                            try:
                                return obj.index(idx, start)
                            except ValueError:
                                return -1
                        elif member == 'charCodeAt':
                            assertion(isinstance(obj, str), 'must be applied on a string')
                            assertion(len(argvals) == 1, 'takes exactly one argument')
                            idx = argvals[0] if isinstance(argvals[0], int) else 0
                            if idx >= len(obj):
                                return None
                            return ord(obj[idx])

                        idx = int(member) if isinstance(obj, list) else member
                        return obj[idx](argvals, allow_recursion=allow_recursion)

                    if remaining:
                        ret, should_abort = self.interpret_statement(
                            self._named_object(local_vars, eval_method()) + remaining,
                            local_vars, allow_recursion)
                        return ret, should_return or should_abort
                    else:
                        return eval_method(), should_return

                elif m and m.group('function'):
                    fname = m.group('fname')
                    argvals = [self.interpret_expression(v, local_vars, allow_recursion)
                            for v in self._separate(m.group('args'))]
                    if fname in local_vars:
                        return local_vars[fname](argvals, allow_recursion=allow_recursion), should_return
                    elif fname not in self._functions:
                        self._functions[fname] = self.extract_function(fname)
                    return self._functions[fname](argvals, allow_recursion=allow_recursion), should_return

                raise self.Exception(
                    f'Unsupported JS expression {truncate_string(expr, 20, 20) if expr != stmt else ""}', stmt)

            def interpret_expression(self, expr, local_vars, allow_recursion):
                ret, should_return = self.interpret_statement(expr, local_vars, allow_recursion)
                if should_return:
                    raise self.Exception('Cannot return from an expression', expr)
                return ret

            def extract_object(self, objname):
                _FUNC_NAME_RE = r'''(?:[a-zA-Z$0-9]+|"[a-zA-Z$0-9]+"|'[a-zA-Z$0-9]+')'''
                obj = {}
                obj_m = re.search(
                    r'''(?x)
                        (?<!\.)%s\s*=\s*{\s*
                            (?P<fields>(%s\s*:\s*function\s*\(.*?\)\s*{.*?}(?:,\s*)?)*)
                        }\s*;
                    ''' % (re.escape(objname), _FUNC_NAME_RE),
                    self.code)
                if not obj_m:
                    raise self.Exception(f'Could not find object {objname}')
                fields = obj_m.group('fields')
                # Currently, it only supports function definitions
                fields_m = re.finditer(
                    r'''(?x)
                        (?P<key>%s)\s*:\s*function\s*\((?P<args>(?:%s|,)*)\){(?P<code>[^}]+)}
                    ''' % (_FUNC_NAME_RE, _NAME_RE),
                    fields)
                for f in fields_m:
                    argnames = f.group('args').split(',')
                    name = remove_quotes(f.group('key'))
                    obj[name] = function_with_repr(self.build_function(argnames, f.group('code')), f'F<{name}>')

                return obj

            def extract_function_code(self, funcname):
                """ @returns argnames, code """
                func_m = re.search(
                    r'''(?xs)
                        (?:
                            function\s+%(name)s|
                            [{;,]\s*%(name)s\s*=\s*function|
                            (?:var|const|let)\s+%(name)s\s*=\s*function
                        )\s*
                        \((?P<args>[^)]*)\)\s*
                        (?P<code>{.+})''' % {'name': re.escape(funcname)},
                    self.code)
                if func_m is None:
                    raise self.Exception(f'Could not find JS function "{funcname}"')
                code, _ = self._separate_at_paren(func_m.group('code'))
                return [x.strip() for x in func_m.group('args').split(',')], code

            def extract_function(self, funcname):
                return function_with_repr(
                    self.extract_function_from_code(*self.extract_function_code(funcname)),
                    f'F<{funcname}>')

            def extract_function_from_code(self, argnames, code, *global_stack):
                local_vars = {}
                while True:
                    mobj = re.search(r'function\((?P<args>[^)]*)\)\s*{', code)
                    if mobj is None:
                        break
                    start, body_start = mobj.span()
                    body, remaining = self._separate_at_paren(code[body_start - 1:])
                    name = self._named_object(local_vars, self.extract_function_from_code(
                        [x.strip() for x in mobj.group('args').split(',')],
                        body, local_vars, *global_stack))
                    code = code[:start] + name + remaining
                return self.build_function(argnames, code, local_vars, *global_stack)

            def call_function(self, funcname, *args):
                return self.extract_function(funcname)(args)

            def build_function(self, argnames, code, *global_stack):
                global_stack = list(global_stack) or [{}]
                argnames = tuple(argnames)

                def resf(args, kwargs={}, allow_recursion=100):
                    global_stack[0].update(itertools.zip_longest(argnames, args, fillvalue=None))
                    global_stack[0].update(kwargs)
                    var_stack = LocalNameSpace(*global_stack)
                    ret, should_abort = self.interpret_statement(code.replace('\n', ' '), var_stack, allow_recursion - 1)
                    if should_abort:
                        return ret
                return resf      
        return JSInterpreter(jsCode)  



    def traverse_obj(
            obj, *path_list, default=None, expected_type=None, get_all=True,
            casesense=True, is_user_input=False, traverse_string=False):
        ''' Traverse nested list/dict/tuple
        @param path_list        A list of paths which are checked one by one.
                                Each path is a list of keys where each key is a string,
                                a function, a tuple of strings or "...".
                                When a fuction is given, it takes the key as argument and
                                returns whether the key matches or not. When a tuple is given,
                                all the keys given in the tuple are traversed, and
                                "..." traverses all the keys in the object
        @param default          Default value to return
        @param expected_type    Only accept final value of this type (Can also be any callable)
        @param get_all          Return all the values obtained from a path or only the first one
        @param casesense        Whether to consider dictionary keys as case sensitive
        @param is_user_input    Whether the keys are generated from user input. If True,
                                strings are converted to int/slice if necessary
        @param traverse_string  Whether to traverse inside strings. If True, any
                                non-compatible object will also be converted into a string
        # TODO: Write tests
        '''
        import collections
        import itertools
        class LazyList(collections.abc.Sequence):
            ''' Lazy immutable list from an iterable
            Note that slices of a LazyList are lists and not LazyList'''
            class IndexError(IndexError):
                pass
            def __init__(self, iterable):
                self.__iterable = iter(iterable)
                self.__cache = []
                self.__reversed = False
            def __iter__(self):
                if self.__reversed:
                    # We need to consume the entire iterable to iterate in reverse
                    yield from self.exhaust()
                    return
                yield from self.__cache
                for item in self.__iterable:
                    self.__cache.append(item)
                    yield item
            def __exhaust(self):
                self.__cache.extend(self.__iterable)
                return self.__cache
            def exhaust(self):
                ''' Evaluate the entire iterable '''
                return self.__exhaust()[::-1 if self.__reversed else 1]
            @staticmethod
            def __reverse_index(x):
                return None if x is None else -(x + 1)
            def __getitem__(self, idx):
                if isinstance(idx, slice):
                    if self.__reversed:
                        idx = slice(self.__reverse_index(idx.start), self.__reverse_index(idx.stop), -(idx.step or 1))
                    start, stop, step = idx.start, idx.stop, idx.step or 1
                elif isinstance(idx, int):
                    if self.__reversed:
                        idx = self.__reverse_index(idx)
                    start, stop, step = idx, idx, 0
                else:
                    raise TypeError('indices must be integers or slices')
                if ((start or 0) < 0 or (stop or 0) < 0
                        or (start is None and step < 0)
                        or (stop is None and step > 0)):
                    # We need to consume the entire iterable to be able to slice from the end
                    # Obviously, never use this with infinite iterables
                    self.__exhaust()
                    try:
                        return self.__cache[idx]
                    except IndexError as e:
                        raise self.IndexError(e) from e
                n = max(start or 0, stop or 0) - len(self.__cache) + 1
                if n > 0:
                    self.__cache.extend(itertools.islice(self.__iterable, n))
                try:
                    return self.__cache[idx]
                except IndexError as e:
                    raise self.IndexError(e) from e
            def __bool__(self):
                try:
                    self[-1] if self.__reversed else self[0]
                except self.IndexError:
                    return False
                return True
            def __len__(self):
                self.__exhaust()
                return len(self.__cache)
            def reverse(self):
                self.__reversed = not self.__reversed
                return self
            def __repr__(self):
                # repr and str should mimic a list. So we exhaust the iterable
                return repr(self.exhaust())
            def __str__(self):
                return repr(self.exhaust())
        def variadic(x, allowed_types=(str, bytes)):
            return x if isinstance(x, collections.abc.Iterable) and not isinstance(x, allowed_types) else (x,)
        if not casesense:
            _lower = lambda k: (k.lower() if isinstance(k, str) else k)
            path_list = (map(_lower, variadic(path)) for path in path_list)
        def _traverse_obj(obj, path, _current_depth=0):
            nonlocal depth
            if obj is None:
                return None
            path = tuple(variadic(path))
            for i, key in enumerate(path):
                if isinstance(key, (list, tuple)):
                    obj = [_traverse_obj(obj, sub_key, _current_depth) for sub_key in key]
                    key = ...
                if key is ...:
                    obj = (obj.values() if isinstance(obj, dict)
                        else obj if isinstance(obj, (list, tuple, LazyList))
                        else str(obj) if traverse_string else [])
                    _current_depth += 1
                    depth = max(depth, _current_depth)
                    return [_traverse_obj(inner_obj, path[i + 1:], _current_depth) for inner_obj in obj]
                elif callable(key):
                    if isinstance(obj, (list, tuple, LazyList)):
                        obj = enumerate(obj)
                    elif isinstance(obj, dict):
                        obj = obj.items()
                    else:
                        if not traverse_string:
                            return None
                        obj = str(obj)
                    _current_depth += 1
                    depth = max(depth, _current_depth)
                    return [_traverse_obj(v, path[i + 1:], _current_depth) for k, v in obj if key(k)]
                elif isinstance(obj, dict) and not (is_user_input and key == ':'):
                    obj = (obj.get(key) if casesense or (key in obj)
                        else next((v for k, v in obj.items() if _lower(k) == key), None))
                else:
                    if is_user_input:
                        key = (int_or_none(key) if ':' not in key
                            else slice(*map(int_or_none, key.split(':'))))
                        if key == slice(None):
                            temp = [...]
                            temp.extend(list(path[i + 1:]))
                            return _traverse_obj(obj, tuple(temp), _current_depth) 
                    if not isinstance(key, (int, slice)):
                        return None
                    if not isinstance(obj, (list, tuple, LazyList)):
                        if not traverse_string:
                            return None
                        obj = str(obj)
                    try:
                        obj = obj[key]
                    except IndexError:
                        return None
            return obj
        if isinstance(expected_type, type):
            type_test = lambda val: val if isinstance(val, expected_type) else None
        elif expected_type is not None:
            type_test = expected_type
        else:
            type_test = lambda val: val
        for path in path_list:
            depth = 0
            val = _traverse_obj(obj, path)
            if val is not None:
                if depth:
                    for _ in range(depth - 1):
                        val = itertools.chain.from_iterable(v for v in val if v is not None)
                    val = [v for v in map(type_test, val) if v is not None]
                    if val:
                        return val if get_all else val[0]
                else:
                    val = type_test(val)
                    if val is not None:
                        return val
        return default
    NO_DEFAULT = object()
    def dict_get(d, key_or_keys, default=None, skip_false_values=True):
        if isinstance(key_or_keys, (list, tuple)):
            for key in key_or_keys:
                if key not in d or d[key] is None or skip_false_values and not d[key]:
                    continue
                return d[key]
            return default
        return d.get(key_or_keys, default)
    def str_or_none(v, default=None):
        return default if v is None else compat_str(v)        
    def url_or_none(url):
        if not url or not isinstance(url, compat_str):
            return None
        url = url.strip()
        return url if re.match(r'^(?:[a-zA-Z][\da-zA-Z.+-]*:)?//', url) else None
       
    class YoutubeIE(BaseCLS):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._code_cache = {}
            self._player_cache = {}
        def _download_webpage(self, url_or_request, video_id, note=None, errnote=None, fatal=True, tries=1, timeout=5, encoding=None, data=None, headers={}, query={}):
            try:
                bFatal = fatal
                if url_or_request.find('//www.youtube.com/get_video_info') > -1 and not fatal:
                    bFatal = True
                result = super(YoutubeIE, self)._download_webpage(url_or_request, video_id, note=note, errnote=errnote, fatal=bFatal, tries=tries, timeout=timeout, encoding=encoding, data=data, headers=headers, query=query)
                if result and result.find('Sorry for the interruption. We have been receiving a large volume of requests from your network') > -1:
                    raise Exception('HTTP Error 429')
                return result                    
            except Exception as ex:
                message = str(ex)
                #if message.find('HTTP Error 429') > -1:
                #    self._downloader.params['source_address'] = ''
                if message.find('400: Bad Request') > -1:
                    self._downloader.cookiejar.clear()
                return super(YoutubeIE, self)._download_webpage(url_or_request, video_id, note=note, errnote=errnote, fatal=fatal, tries=tries, timeout=timeout, encoding=encoding, data=data, headers=headers, query=query)
        def _parse_sig_js(self, jscode):
            funcname = self._search_regex(
                (r'\b[cs]\s*&&\s*[adf]\.set\([^,]+\s*,\s*encodeURIComponent\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(',
                r'\b[a-zA-Z0-9]+\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*encodeURIComponent\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(',
                r'\bm=(?P<sig>[a-zA-Z0-9$]{2,})\(decodeURIComponent\(h\.s\)\)',
                r'\bc&&\(c=(?P<sig>[a-zA-Z0-9$]{2,})\(decodeURIComponent\(c\)\)',
                r'(?:\b|[^a-zA-Z0-9$])(?P<sig>[a-zA-Z0-9$]{2,})\s*=\s*function\(\s*a\s*\)\s*{\s*a\s*=\s*a\.split\(\s*""\s*\)(?:;[a-zA-Z0-9$]{2}\.[a-zA-Z0-9$]{2}\(a,\d+\))?',
                r'(?:\b|[^a-zA-Z0-9$])(?P<sig>[a-zA-Z0-9$]{2})\s*=\s*function\(\s*a\s*\)\s*{\s*a\s*=\s*a\.split\(\s*""\s*\)',
                r'(?P<sig>[a-zA-Z0-9$]+)\s*=\s*function\(\s*a\s*\)\s*{\s*a\s*=\s*a\.split\(\s*""\s*\)',
                # Obsolete patterns
                r'("|\')signature\1\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(',
                r'\.sig\|\|(?P<sig>[a-zA-Z0-9$]+)\(',
                r'yt\.akamaized\.net/\)\s*\|\|\s*.*?\s*[cs]\s*&&\s*[adf]\.set\([^,]+\s*,\s*(?:encodeURIComponent\s*\()?\s*(?P<sig>[a-zA-Z0-9$]+)\(',
                r'\b[cs]\s*&&\s*[adf]\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(',
                r'\b[a-zA-Z0-9]+\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(',
                r'\bc\s*&&\s*a\.set\([^,]+\s*,\s*\([^)]*\)\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(',
                r'\bc\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*\([^)]*\)\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(',
                r'\bc\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*\([^)]*\)\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\('),
                jscode, 'Initial JS player signature function name', group='sig')
            # jsi = CreateJSInterpreter(jscode)
            jsi = CreateJSInterpreterEx(jscode)
            initial_function = jsi.extract_function(funcname)
            return lambda s: initial_function([s])
        def _is_valid_url(self, url, video_id, item='video', headers={}):
            import sys
            if sys.platform == 'darwin':                
                print('mac call super _is_valid_url')
                return super()._is_valid_url(url, video_id, item, headers)
 
            try:
                import urllib.request
                req = urllib.request.Request(url, method='HEAD')
                head_response = urllib.request.urlopen(req)
                return head_response.code == 200
                # return super(YoutubeIE, self)._is_valid_url(url, video_id, item, headers)
            except:
                return False
        def _check_formats(self, formats, video_id):
            def check_format(f):
                result = self._is_valid_url(f['url'], video_id,
                    item='%s video format' % f.get('format_id') if f.get('format_id') else 'video')
                if not result and 'fragments' in f and len(f['fragments'])>0:
                    try:
                        print('---begin check fragments url---')
                        result = self._is_valid_url(f['fragments'][0]['url'], video_id,
                            item='%s video format' % f.get('format_id') if f.get('format_id') else 'video')
                        print('---end check fragments url---')
                    except:
                        pass
                return result
            if formats:
                formats[:] = filter(
                    lambda f: check_format(f),
                    formats)
        def convertToDash(self, f):
            if 'fragments' in f:
                print(f['format_id'], 'has fragments')
                return
            if 'none' not in [f.get('acodec', 'none'), f.get('vcodec', 'none')]:
                print(f['format_id'], 'not dash')
                return
            try:
                url = f['url']
                clen = self._search_regex(r'clen=(\d+)', url, '', fatal=False)
                if clen:
                    fragments = []
                    mediaLen = int(clen)
                    segmentLen = 2 * 1024 * 1024 if f.get('acodec', 'none') else 1 * 1024 * 1024
                    segmentCount = math.ceil(mediaLen / segmentLen)
                    print(f['format_id'], 'mediaLen: %d segmentCount: %d' % (mediaLen, segmentCount))
                    if segmentCount > 0:
                        end = 0
                        for i in range(segmentCount):
                            start = 0 if i ==0 else end + 1
                            end = start + segmentLen
                            fragments.append({'url': '%s&range=%s-%s' % (url, start, end)})
                        if end < mediaLen:
                            fragments.append({'url': '%s&range=%s-%s' % (url, end + 1, mediaLen)})
                        f['fragments'] = fragments
                        # f.pop('url')
                        # f['protocol'] = 'https'
            except:
                pass

        def _initialize_consent(self):
            cookies = self._get_cookies('https://www.youtube.com/')
            if cookies.get('__Secure-3PSID'):
                return
            socs = cookies.get('SOCS')
            if socs and not socs.value.startswith('CAA'):  # not consented
                return
            self._set_cookie('.youtube.com', 'SOCS', 'CAI', secure=True)  # accept all (required for mixes)

        def _reportFailReason(self, video_info, video_webpage, video_id):
            token = video_info.get('token') or video_info.get('account_playback_token')
            if not token:
                if 'reason' in video_info:
                    if 'The uploader has not made this video available in your country.' in video_info['reason']:
                        regions_allowed = self._html_search_meta(
                            'regionsAllowed', video_webpage, default=None)
                        countries = regions_allowed.split(',') if regions_allowed else None
                        self.raise_geo_restricted(
                            msg=video_info['reason'][0], countries=countries)
                    raise ExtractorError(
                        'YouTube said: %s' % video_info['reason'][0],
                        expected=True, video_id=video_id)
                else:
                    raise ExtractorError('"token" parameter not in video info for unknown reason', video_id=video_id)     

        def _import_cookie(self):
            cookies = [
                {"name": "CONSENT", "value": "PENDING+459", "domain": "youtube.com"},
                {"name": "PREF", "value": "f7=4100&tz=UTC&f4=4000000&hl=en", "domain": "youtube.com"},
                {"name": "VISITOR_INFO1_LIVE", "value": "JZxhrZk24nU", "domain": "youtube.com"},
                {"name": "VISITOR_PRIVACY_METADATA", "value": "CgJISxIEGgAgOw%3D%3D", "domain": "youtube.com"},
                {"name": "YSC", "value": "ZUrl3R_NEc0", "domain": "youtube.com"},
                {"name": "SOCS", "value": "CAI", "domain": "youtube.com"},
            ]

            # 将cookies添加到CookieJar
            for cookie in cookies:
                self._set_cookie('youtube.com', cookie["name"], cookie["value"])
                          

        def _real_extract(self, url):
            #self._import_cookie()
            self._initialize_consent()
            self._YT_INITIAL_PLAYER_RESPONSE_RE = r'ytInitialPlayerResponse\s*=\s*({.+?})\s*;'
            self._YT_INITIAL_BOUNDARY_RE = r'(?:var\s+meta|</script|\n)'        
            url, smuggled_data = unsmuggle_url(url, {})
            proto = 'https'
            # Extract original video URL from URL with redirection, like age verification, using next_url parameter
            mobj = re.search(self._NEXT_URL_RE, url)
            if mobj:
                url = proto + '://www.youtube.com/' + compat_urllib_parse_unquote(mobj.group(1)).lstrip('/')
            video_id = self.extract_id(url)
            # Get video webpage
            url = proto + '://www.youtube.com/watch?v=%s&gl=US&hl=en&has_verified=1&bpctr=9999999999' % video_id
            video_webpage = self._download_webpage(url, video_id, tries=3)
            # file = open(r'e:\1\ytdlp2.html', "r", encoding='utf-8')
            # video_webpage = file.read()
            # file.close()
            # end
            player_response = {}
            # Get video info
            embed_webpage = None       
            def extract_player_response(player_response, video_id):
                pl_response = str_or_none(player_response)
                if not pl_response:
                    return
                pl_response = self._parse_json(pl_response, video_id, fatal=False)
                if isinstance(pl_response, dict):
                    return pl_response
                    
            if re.search(r'player-age-gate-content">', video_webpage) is not None:
                age_gate = True
                # We simulate the access to the video from www.youtube.com/v/{video_id}
                # this can be viewed without login into Youtube
                url = proto + '://www.youtube.com/embed/%s' % video_id
                embed_webpage = self._download_webpage(url, video_id, 'Downloading embed webpage')
                data = compat_urllib_parse_urlencode({
                    'video_id': video_id,
                    'eurl': 'https://youtube.googleapis.com/v/' + video_id,
                    'sts': self._search_regex(
                        r'"sts"\s*:\s*(\d+)', embed_webpage, 'sts', default=''),
                })
                video_info_url = proto + '://www.youtube.com/get_video_info?' + data
                video_info_webpage = self._download_webpage(
                    video_info_url, video_id,
                    note='Refetching age-gated info webpage',
                    errnote='unable to download video info webpage')
                video_info = compat_parse_qs(video_info_webpage)
                pl_response = video_info.get('player_response', [None])[0]
                player_response = extract_player_response(pl_response, video_id)                
            else:
                age_gate = False
                video_info = None
                sts = ''
                # Try looking directly into the video webpage
                ytplayer_config = self._get_ytplayer_config(video_id, video_webpage)
                if ytplayer_config:
                    args = ytplayer_config['args']
                    if args.get('url_encoded_fmt_stream_map') or args.get('hlsvp'):
                        # Convert to the same format returned by compat_parse_qs
                        video_info = dict((k, [v]) for k, v in args.items())
                    # Rental video is not rented but preview is available (e.g.
                    # https://www.youtube.com/watch?v=yYr8q0y5Jfg,
                    # https://github.com/rg3/youtube-dl/issues/10532)
                    if not video_info and args.get('ypc_vid'):
                        return self.url_result(
                            args['ypc_vid'], YoutubeIE.ie_key(), video_id=args['ypc_vid'])
                    if args.get('livestream') == '1' or args.get('live_playback') == 1:
                        is_live = True
                    # sts = ytplayer_config.get('sts', '')
                    if not player_response:
                        player_response = extract_player_response(args.get('player_response'), video_id)
            self._YT_INITIAL_PLAYER_RESPONSE_RE = r'ytInitialPlayerResponse\s*=\s*({.+?})\s*;'
            if not video_info and not player_response:
                player_response = extract_player_response(
                    self._search_regex(
                        (r'%s\s*(?:var\s+meta|</script|\n)' % self._YT_INITIAL_PLAYER_RESPONSE_RE,
                        self._YT_INITIAL_PLAYER_RESPONSE_RE), video_webpage,
                        'initial player response', default='{}'),
                    video_id)            
            def extract_unavailable_message():
              return self._html_search_regex(r'(?s)<h1[^>]+id="unavailable-message"[^>]*>(.+?)</h1>',
                video_webpage, 'unavailable message', default=None)
            if not video_info and not player_response:
                unavailable_message = extract_unavailable_message()
                if not unavailable_message:
                    unavailable_message = 'Unable to extract video data'
                raise ExtractorError(
                    'YouTube said: %s' % unavailable_message, expected=True, video_id=video_id)   
            if not isinstance(video_info, dict):
                video_info = {}
            video_details = try_get(
                player_response, lambda x: x['videoDetails'], dict) or {}
            # title
            video_title = video_info.get('title', [None])[0] or video_details.get('title')
            if not video_title:
                self._downloader.report_warning('Unable to extract video title')
                video_title = '_'
            if 'multifeed_metadata_list' in video_info and not smuggled_data.get('force_singlefeed', False):
                if not self._downloader.params.get('noplaylist'):
                    entries = []
                    feed_ids = []
                    multifeed_metadata_list = video_info['multifeed_metadata_list'][0]
                    for feed in multifeed_metadata_list.split(','):
                        # Unquote should take place before split on comma (,) since textual
                        # fields may contain comma as well (see
                        # https://github.com/rg3/youtube-dl/issues/8536)
                        feed_data = compat_parse_qs(compat_urllib_parse_unquote_plus(feed))
                        entries.append({
                            '_type': 'url_transparent',
                            'ie_key': 'Youtube',
                            'url': smuggle_url(
                                '%s://www.youtube.com/watch?v=%s' % (proto, feed_data['id'][0]),
                                {'force_singlefeed': True}),
                            'title': '%s (%s)' % (video_title, feed_data['title'][0]),
                        })
                        feed_ids.append(feed_data['id'][0])
                    self.to_screen(
                        'Downloading multifeed video (%s) - add --no-playlist to just download video %s'
                        % (', '.join(feed_ids), video_id))
                    return self.playlist_result(entries, video_id, video_title, '')
                self.to_screen('Downloading just video %s because of --no-playlist' % video_id)
            mobj = re.search(
                r'<link itemprop="url" href="(?P<uploader_url>https?://www.youtube.com/(?:user|channel)/(?P<uploader_id>[^"]+))">',
                video_webpage)
            # thumbnail image
            # We try first to get a high quality image:
            m_thumb = re.search(r'<span itemprop="thumbnail".*?href="(.*?)">',
                                video_webpage, re.DOTALL)
            if m_thumb is not None:
                video_thumbnail = m_thumb.group(1)
            elif 'thumbnail_url' not in video_info:
                self._downloader.report_warning('unable to extract video thumbnail')
                video_thumbnail = None
            else:   # don't panic if we can't find it
                video_thumbnail = compat_urllib_parse_unquote_plus(video_info['thumbnail_url'][0])
            video_duration = try_get(
                video_info, lambda x: int_or_none(x['length_seconds'][0]))
            if not video_duration:
                video_duration = parse_duration(self._html_search_meta(
                    'duration', video_webpage, 'video duration'))
            formats = self._extractFormatFromAPI(url, video_webpage, embed_webpage, video_id, age_gate, smuggled_data)
            time_out = self._downloader._socket_timeout
            self._downloader._socket_timeout = 3
            self._check_formats(formats, video_id)
            self._downloader._socket_timeout = time_out
            self._sort_formats(formats)
            for format in formats:
                if ('vcodec' in format) and format.get('vcodec', 'none') != 'none' and ('acodec' in format) and format.get('acodec', 'none') != 'none':
                    format['preference'] = 1
            ##filter short
            format2 = []
            # for f in formats:                
            #     try:
            #         dur = self._search_regex(r'&dur=([^&=]+)', f['url'], '')
            #         if dur and float(dur) <= video_duration*3/4: continue
            #         format2.append(f)
            #     except:
            #         format2.append(f)
            #         pass
            formats = format2 if format2 else formats
            if not formats:
                self._reportFailReason(video_info, video_webpage, video_id)
            return {
                'id': video_id,
                'title': video_title,
                'thumbnail': video_thumbnail,
                'duration': video_duration,
                'age_limit': 18 if age_gate else 0,
                'webpage_url': proto + '://www.youtube.com/watch?v=%s' % video_id,
                'formats': formats,
            }
        def _get_innertube_host(self, client='web'):
            return INNERTUBE_CLIENTS[client]['INNERTUBE_HOST']
        def _extract_client_version(self, ytcfg, default_client='web'):
            return self._ytcfg_get_safe(
                ytcfg, (lambda x: x['INNERTUBE_CLIENT_VERSION'],
                        lambda x: x['INNERTUBE_CONTEXT']['client']['clientVersion']), compat_str, default_client)
        def _extract_api_key(self, ytcfg=None, default_client='web'):
            return self._ytcfg_get_safe(ytcfg, lambda x: x['INNERTUBE_API_KEY'], compat_str, default_client)
        def _extract_identity_token(self, ytcfg=None, webpage=None):
            if ytcfg:
                token = try_get(ytcfg, lambda x: x['ID_TOKEN'], compat_str)
                if token:
                    return token
            if webpage:
                return self._search_regex(
                    r'\bID_TOKEN["\']\s*:\s*["\'](.+?)["\']', webpage,
                    'identity token', default=None, fatal=False)
        def _ytcfg_get_safe(self, ytcfg, getter, expected_type=None, default_client='web'):
            # try_get but with fallback to default ytcfg client values when present
            _func = lambda y: try_get(y, getter, expected_type)
            return _func(ytcfg) or _func(self._get_default_ytcfg(default_client))            
        @property
        def is_authenticated(self):
            return bool(self._generate_sapisidhash_header())
        _SAPISID = None
        def _generate_sapisidhash_header(self, origin='https://www.youtube.com'):
            import time
            time_now = round(time.time())
                       
            if self._SAPISID is None:
                yt_cookies = self._get_cookies('https://www.youtube.com')
                # Sometimes SAPISID cookie isn't present but __Secure-3PAPISID is.
                # See: https://github.com/yt-dlp/yt-dlp/issues/393
                sapisid_cookie = dict_get(
                    yt_cookies, ('__Secure-3PAPISID', 'SAPISID'))
                if sapisid_cookie and sapisid_cookie.value:
                    self._SAPISID = sapisid_cookie.value
                    # self.write_debug('Extracted SAPISID cookie')
                    # SAPISID cookie is required if not already present
                    if not yt_cookies.get('SAPISID'):
                        # self.write_debug('Copying __Secure-3PAPISID cookie to SAPISID cookie')
                        self._set_cookie(
                            '.youtube.com', 'SAPISID', self._SAPISID, secure=True, expire_time=time_now + 3600)
                else:
                    self._SAPISID = False
            if not self._SAPISID:
                return None
            # SAPISIDHASH algorithm from https://stackoverflow.com/a/32065323
            import hashlib
            sapisidhash = hashlib.sha1(('%d %s %s' % (time_now, self._SAPISID, origin)).encode('utf-8')).hexdigest()
            return 'SAPISIDHASH %d_%s' % (time_now, sapisidhash)
        def generate_api_headers(
                self, *, ytcfg=None, account_syncid=None, session_index=None,
                visitor_data=None, identity_token=None, api_hostname=None, default_client='web'):
            origin = 'https://' + (api_hostname if api_hostname else self._get_innertube_host(default_client))
            headers = {
                'X-YouTube-Client-Name': compat_str(
                    self._ytcfg_get_safe(ytcfg, lambda x: x['INNERTUBE_CONTEXT_CLIENT_NAME'], default_client=default_client)),
                'X-YouTube-Client-Version': self._extract_client_version(ytcfg, default_client),
                'Origin': origin,
                'X-Youtube-Identity-Token': identity_token or self._extract_identity_token(ytcfg),
                # 'X-Goog-PageId': account_syncid or self._extract_account_syncid(ytcfg),
                # 'X-Goog-Visitor-Id': visitor_data or self._extract_visitor_data(ytcfg)
                'User-Agent': self._ytcfg_get_safe(ytcfg, lambda x: x['INNERTUBE_CONTEXT']['client']['userAgent'],
                                                   default_client=default_client)
            }
            if session_index is None:
                session_index = self._extract_session_index(ytcfg)
            if account_syncid or session_index is not None:
                headers['X-Goog-AuthUser'] = session_index if session_index is not None else 0
            auth = self._generate_sapisidhash_header(origin)
            if auth is not None:
                headers['Authorization'] = auth
                headers['X-Origin'] = origin
            return {h: v for h, v in headers.items() if v is not None}
        def _call_api(self, ep, query, video_id, fatal=True, headers=None,
                    note='Downloading API JSON', errnote='Unable to download API page',
                    context=None, api_key=None, api_hostname=None, default_client='web'):
            data = {'context': context} if context else {'context': self._extract_context(default_client=default_client)}
            data.update(query)
            real_headers = self.generate_api_headers(default_client=default_client)
            real_headers.update({'content-type': 'application/json'})
            if headers:
                real_headers.update(headers)
            return self._download_json(
                'https://%s/youtubei/v1/%s' % (api_hostname or self._get_innertube_host(default_client), ep),
                video_id=video_id, fatal=fatal, note=note, errnote=errnote,
                data=json.dumps(data).encode('utf8'), headers=real_headers,
                query={'key': api_key or self._extract_api_key(), 'prettyPrint': 'false'})
        @staticmethod
        def _extract_session_index(*data):
            """
            Index of current account in account list.
            See: https://github.com/yt-dlp/yt-dlp/pull/519
            """
            for ytcfg in data:
                session_index = int_or_none(try_get(ytcfg, lambda x: x['SESSION_INDEX']))
                if session_index is not None:
                    return session_index  
        @staticmethod
        def _extract_account_syncid(*args):
            """
            Extract syncId required to download private playlists of secondary channels
            @params response and/or ytcfg
            """
            for data in args:
                # ytcfg includes channel_syncid if on secondary channel
                delegated_sid = try_get(data, lambda x: x['DELEGATED_SESSION_ID'], compat_str)
                if delegated_sid:
                    return delegated_sid
                sync_ids = (try_get(
                    data, (lambda x: x['responseContext']['mainAppWebResponseContext']['datasyncId'],
                        lambda x: x['DATASYNC_ID']), compat_str) or '').split('||')
                if len(sync_ids) >= 2 and sync_ids[1]:
                    # datasyncid is of the form "channel_syncid||user_syncid" for secondary channel
                    # and just "user_syncid||" for primary channel. We only want the channel_syncid
                    return sync_ids[0]                              
        @staticmethod
        def _get_checkok_params():
            return {'contentCheckOk': True, 'racyCheckOk': True}
        @staticmethod
        def _extract_visitor_data(*args):
            """
            Extracts visitorData from an API response or ytcfg
            Appears to be used to track session state
            """
            return traverse_obj(
                args, (..., ('VISITOR_DATA', ('INNERTUBE_CONTEXT', 'client', 'visitorData'), ('responseContext', 'visitorData'))),
                expected_type=compat_str, get_all=False)
        @classmethod
        def _generate_player_context(cls, sts=None):
            context = {
                'html5Preference': 'HTML5_PREF_WANTS',
            }
            if sts is not None:
                context['signatureTimestamp'] = sts
            return {
                'playbackContext': {
                    'contentPlaybackContext': context
                },
                'contentCheckOk': True, 
                'racyCheckOk': True
            }  
        @staticmethod
        def _is_unplayable(player_response):
            return traverse_obj(player_response, ('playabilityStatus', 'status')) == 'UNPLAYABLE'                  
        @staticmethod
        def is_music_url(url):
            return re.match(r'https?://music\.youtube\.com/', url) is not None
        @staticmethod
        def orderedSet(iterable):
            """ Remove all duplicates from the input iterable """
            res = []
            for el in iterable:
                if el not in res:
                    res.append(el)
            return res
        def _load_player(self, video_id, player_url, fatal=True):
            player_id = self._extract_player_info(player_url)
            if player_id not in self._code_cache:
                code = self._download_webpage(
                    player_url, video_id, fatal=fatal,
                    note='Downloading player ' + player_id,
                    errnote='Download of %s failed' % player_url)
                if code:
                    self._code_cache[player_id] = code
            return self._code_cache.get(player_id)
        @staticmethod
        def _is_agegated(player_response):
            if traverse_obj(player_response, ('playabilityStatus', 'desktopLegacyAgeGateReason')):
                return True
            reasons = traverse_obj(player_response, ('playabilityStatus', ('status', 'reason')), default=[])
            AGE_GATE_REASONS = (
                'confirm your age', 'age-restricted', 'inappropriate',  # reason
                'age_verification_required', 'age_check_required',  # status
            )
            return any(expected in reason for expected in AGE_GATE_REASONS for reason in reasons)            
        def _extract_client_name(self, ytcfg, default_client='web'):
            return self._ytcfg_get_safe(
                ytcfg, (lambda x: x['INNERTUBE_CLIENT_NAME'],
                        lambda x: x['INNERTUBE_CONTEXT']['client']['clientName']), compat_str, default_client)
            
        def get_param(self, name, default=None, *args, **kwargs):
            if self._downloader:
                return self._downloader.params.get(name, default, *args, **kwargs)
            return default  
        def _extract_context(self, ytcfg=None, default_client='web'):
            _get_context = lambda y: try_get(y, lambda x: x['INNERTUBE_CONTEXT'], dict)
            context = _get_context(ytcfg)
            if context:
                return context
            context = _get_context(self._get_default_ytcfg(default_client))
            if not ytcfg:
                return context
            # Recreate the client context (required)
            context['client'].update({
                'clientVersion': self._extract_client_version(ytcfg, default_client),
                'clientName': self._extract_client_name(ytcfg, default_client),
            })
            visitor_data = try_get(ytcfg, lambda x: x['VISITOR_DATA'], compat_str)
            if visitor_data:
                context['client']['visitorData'] = visitor_data
            return context  
        def _report_alerts(self, alerts, expected=True, fatal=True, only_once=False):
            errors = []
            warnings = []
            for alert_type, alert_message in alerts:
                if alert_type.lower() == 'error' and fatal:
                    errors.append([alert_type, alert_message])
                else:
                    warnings.append([alert_type, alert_message])
            for alert_type, alert_message in (warnings + errors[:-1]):
                self.report_warning('YouTube said: %s - %s' % (alert_type, alert_message), only_once=only_once)
            if errors:
                raise ExtractorError('YouTube said: %s' % errors[-1][1], expected=expected)
        @classmethod
        def _extract_alerts(cls, data):
            for alert_dict in try_get(data, lambda x: x['alerts'], list) or []:
                if not isinstance(alert_dict, dict):
                    continue
                for alert in alert_dict.values():
                    alert_type = alert.get('type')
                    if not alert_type:
                        continue
                    message = cls._get_text(alert, 'text')
                    if message:
                        yield alert_type, message
        def _extract_and_report_alerts(self, data, *args, **kwargs):
            return self._report_alerts(self._extract_alerts(data), *args, **kwargs)                                
        def _extract_response(self, item_id, query, note='Downloading API JSON', headers=None,
                            ytcfg=None, check_get_keys=None, ep='browse', fatal=True, api_hostname=None,
                            default_client='web'):
            def remove_end(s, end):
                return s[:-len(end)] if s is not None and s.endswith(end) else s                            
            response = None
            last_error = None
            count = -1
            retries = self.get_param('extractor_retries', 3)
            if check_get_keys is None:
                check_get_keys = []
            import socket, urllib, http
            network_exceptions = [urllib.error.URLError, http.client.HTTPException, socket.error]
            compat_HTTPError = urllib.error.HTTPError
            # if hasattr(ssl, 'CertificateError'):
            #     network_exceptions.append(ssl.CertificateError)
            def is_html(first_bytes):
                """ Detect whether a file contains HTML by examining its first bytes. """
                BOMS = [
                    (b'\xef\xbb\xbf', 'utf-8'),
                    (b'\x00\x00\xfe\xff', 'utf-32-be'),
                    (b'\xff\xfe\x00\x00', 'utf-32-le'),
                    (b'\xff\xfe', 'utf-16-le'),
                    (b'\xfe\xff', 'utf-16-be'),
                ]
                for bom, enc in BOMS:
                    if first_bytes.startswith(bom):
                        s = first_bytes[len(bom):].decode(enc, 'replace')
                        break
                else:
                    s = first_bytes.decode('utf-8', 'replace')
                return re.match(r'^\s*<', s)
            def error_to_compat_str(err):
                err_str = str(err)
                return err_str
            network_exceptions = tuple(network_exceptions)                
            while count < retries:
                count += 1
                if last_error:
                    self.report_warning('%s. Retrying ...' % remove_end(last_error, '.'))
                try:
                    response = self._call_api(
                        ep=ep, fatal=True, headers=headers,
                        video_id=item_id, query=query,
                        context=self._extract_context(ytcfg, default_client),
                        api_key=self._extract_api_key(ytcfg, default_client),
                        api_hostname=api_hostname, default_client=default_client,
                        note='%s%s' % (note, ' (retry #%d)' % count if count else ''))
                except ExtractorError as e:
                    if isinstance(e.cause, network_exceptions):
                        if isinstance(e.cause, compat_HTTPError) and not is_html(e.cause.read(512)):
                            e.cause.seek(0)
                            yt_error = try_get(
                                self._parse_json(e.cause.read().decode(), item_id, fatal=False),
                                lambda x: x['error']['message'], compat_str)
                            if yt_error:
                                self._report_alerts([('ERROR', yt_error)], fatal=False)
                        # Downloading page may result in intermittent 5xx HTTP error
                        # Sometimes a 404 is also recieved. See: https://github.com/ytdl-org/youtube-dl/issues/28289
                        # We also want to catch all other network exceptions since errors in later pages can be troublesome
                        # See https://github.com/yt-dlp/yt-dlp/issues/507#issuecomment-880188210
                        if not isinstance(e.cause, compat_HTTPError) or e.cause.code not in (403, 429):
                            last_error = error_to_compat_str(e.cause or e.msg)
                            if count < retries:
                                continue
                    if fatal:
                        raise
                    else:
                        self.report_warning(error_to_compat_str(e))
                        return
                else:
                    try:
                        self._extract_and_report_alerts(response, only_once=True)
                    except ExtractorError as e:
                        # YouTube servers may return errors we want to retry on in a 200 OK response
                        # See: https://github.com/yt-dlp/yt-dlp/issues/839
                        if 'unknown error' in e.msg.lower():
                            last_error = e.msg
                            continue
                        if fatal:
                            raise
                        self.report_warning(error_to_compat_str(e))
                        return
                    if not check_get_keys or dict_get(response, check_get_keys):
                        break
                    # Youtube sometimes sends incomplete data
                    # See: https://github.com/ytdl-org/youtube-dl/issues/28194
                    last_error = 'Incomplete data received'
                    if count >= retries:
                        if fatal:
                            raise ExtractorError(last_error)
                        else:
                            self.report_warning(last_error)
                            return
            return response        
        def _extract_signature_timestamp(self, video_id, player_url, ytcfg=None, fatal=False):
            """
            Extract signatureTimestamp (sts)
            Required to tell API what sig/player version is in use.
            """
            sts = None
            if isinstance(ytcfg, dict):
                sts = int_or_none(ytcfg.get('STS'))
            if not sts:
                # Attempt to extract from player
                if player_url is None:
                    error_msg = 'Cannot extract signature timestamp without player_url.'
                    if fatal:
                        raise ExtractorError(error_msg)
                    self.report_warning(error_msg)
                    return
                if self._load_player(video_id, player_url, fatal=fatal):
                    player_id = self._extract_player_info(player_url)
                    code = self._code_cache[player_id]
                    sts = int_or_none(self._search_regex(
                        r'(?:signatureTimestamp|sts)\s*:\s*(?P<sts>[0-9]{5})', code,
                        'JS player signature timestamp', group='sts', fatal=fatal))
            return sts
        def _extract_yt_initial_variable(self, webpage, regex, video_id, name):
            return self._parse_json(self._search_regex(
                (r'%s\s*%s' % (regex, self._YT_INITIAL_BOUNDARY_RE),
                regex), webpage, name, default='{}'), video_id, fatal=False)
        def _get_default_ytcfg(self, client='web'):
            import copy
            return copy.deepcopy(INNERTUBE_CLIENTS[client])
        def _download_player_url(self, video_id, fatal=False):
            res = self._download_webpage(
                'https://www.youtube.com/iframe_api',
                note='Downloading iframe API JS', video_id=video_id, fatal=fatal)
            if res:
                player_version = self._search_regex(
                    r'player\\?/([0-9a-fA-F]{8})\\?/', res, 'player version', fatal=fatal)
                if player_version:
                    return 'https://www.youtube.com/s/player/%s/player_ias.vflset/en_US/base.js' % player_version
        def _extract_player_url(self, *ytcfgs, webpage=None):
            player_url = traverse_obj(
                ytcfgs, (..., 'PLAYER_JS_URL'), (..., 'WEB_PLAYER_CONTEXT_CONFIGS', ..., 'jsUrl'),
                get_all=False, expected_type=compat_str)
            if not player_url:
                return
            if player_url.startswith('//'):
                player_url = 'https:' + player_url
            elif not re.match(r'https?://', player_url):
                import urllib
                player_url = urllib.parse.urljoin(
                    'https://www.youtube.com', player_url)
            return player_url
        _STORY_PLAYER_PARAMS = 'CgIQBg=='
        def _extract_player_response(self, client, video_id, master_ytcfg, player_ytcfg, player_url, initial_pr):
            session_index = self._extract_session_index(player_ytcfg, master_ytcfg)
            syncid = self._extract_account_syncid(player_ytcfg, master_ytcfg, initial_pr)
            sts = self._extract_signature_timestamp(video_id, player_url, master_ytcfg, fatal=False) if player_url else None
            headers = self.generate_api_headers(
                ytcfg=player_ytcfg, account_syncid=syncid, session_index=session_index, default_client=client)
            yt_query = {'videoId': video_id}
            if _split_innertube_client(client)[0] == 'android':
                yt_query['params'] = self._STORY_PLAYER_PARAMS
            yt_query.update(self._generate_player_context(sts))
            return self._extract_response(
                item_id=video_id, ep='player', query=yt_query,
                ytcfg=player_ytcfg, headers=headers, fatal=True,
                default_client=client,
                note='Downloading %s player API JSON' % client.replace('_', ' ').strip()
            ) or None   
        def extract_ytcfg(self, video_id, webpage):
            if not webpage:
                return {}
            return self._parse_json(
                self._search_regex(
                    r'ytcfg\.set\s*\(\s*({.+?})\s*\)\s*;', webpage, 'ytcfg',
                    default='{}'), video_id, fatal=False) or {} 
        def _configuration_arg(self, key, default=NO_DEFAULT, casesense=False):
                '''
                @returns            A list of values for the extractor argument given by "key"
                                    or "default" if no such key is present
                @param default      The default value to return when the key is not present (default: [])
                @param casesense    When false, the values are converted to lower case
                '''
                val = traverse_obj(
                    self._downloader.params, ('extractor_args', self.ie_key().lower(), key))
                if val is None:
                    return [] if default is NO_DEFAULT else default
                return list(val) if casesense else [x.lower() for x in val]
        def _extract_player_ytcfg(self, client, video_id):
            url = {
                'web': 'https://www.youtube.com',
                'web_music': 'https://music.youtube.com',
                'web_embedded': 'https://www.youtube.com/embed/%s?html5=1' % video_id
            }.get(client)
            if not url:
                return {}
            webpage = self._download_webpage(url, video_id, fatal=False, note='Downloading %s config' % video_id)
            return self.extract_ytcfg(video_id, webpage) or {}
        def _get_requested_clients(self, url, smuggled_data):
            requested_clients = []
            default = ['ios', 'android', 'web']
            allowed_clients = sorted(
                (client for client in INNERTUBE_CLIENTS.keys() if client[:1] != '_'),
                key=lambda client: INNERTUBE_CLIENTS[client]['priority'], reverse=True)
            for client in self._configuration_arg('player_client'):
                if client in allowed_clients:
                    requested_clients.append(client)
                elif client == 'default':
                    requested_clients.extend(default)
                elif client == 'all':
                    requested_clients.extend(allowed_clients)
                else:
                    self.report_warning('Skipping unsupported client {}'.format(client))
            if not requested_clients:
                requested_clients = default
            if smuggled_data.get('is_music_url') or self.is_music_url(url):
                requested_clients.extend(
                    '{}_music'.format(client) for client in requested_clients if '{}_music'.format(client) in INNERTUBE_CLIENTS)
            return self.orderedSet(requested_clients)         
        def _extract_player_responses(self, clients, video_id, webpage, master_ytcfg):
            initial_pr = None
            if webpage:
                initial_pr = self._extract_yt_initial_variable(
                    webpage, self._YT_INITIAL_PLAYER_RESPONSE_RE,
                    video_id, 'initial player response')
            original_clients = clients
            all_clients = set(clients)
            clients = clients[::-1]
            prs = []
            # def append_client(client_name):
            #     if client_name in INNERTUBE_CLIENTS and client_name not in original_clients:
            #         clients.append(client_name)
            def append_client(*client_names):
                """ Append the first client name that exists but not already used """
                for client_name in client_names:
                    actual_client = _split_innertube_client(client_name)[0]
                    if actual_client in INNERTUBE_CLIENTS:
                        if actual_client not in all_clients:
                            clients.append(client_name)
                            all_clients.add(actual_client)
                            return
            # Android player_response does not have microFormats which are needed for
            # extraction of some data. So we return the initial_pr with formats
            # stripped out even if not requested by the user
            # See: https://github.com/yt-dlp/yt-dlp/issues/501
            if initial_pr:
                pr = dict(initial_pr)
                pr['streamingData'] = None
                prs.append(pr)
            last_error = None
            tried_iframe_fallback = False
            player_url = None
            while clients:
                # client = clients.pop()
                client, base_client, variant = _split_innertube_client(clients.pop())
                player_ytcfg = master_ytcfg if client == 'web' else {}
                if 'configs' not in self._configuration_arg('player_skip'):
                    player_ytcfg = self._extract_player_ytcfg(client, video_id) or player_ytcfg
                player_url = player_url or self._extract_player_url(master_ytcfg, player_ytcfg, webpage=webpage)
                require_js_player = self._get_default_ytcfg(client).get('REQUIRE_JS_PLAYER')
                if 'js' in self._configuration_arg('player_skip'):
                    require_js_player = False
                    player_url = None
                if not player_url and not tried_iframe_fallback and require_js_player:
                    player_url = self._download_player_url(video_id)
                    tried_iframe_fallback = True
                try:
                    pr = initial_pr if client == 'web' and initial_pr else self._extract_player_response(
                        client, video_id, player_ytcfg or master_ytcfg, player_ytcfg, player_url if require_js_player else None, initial_pr)
                except ExtractorError as e:
                    if last_error:
                        self.report_warning(last_error)
                    last_error = e
                    continue
                if pr:
                    prs.append(pr)
                # creator clients can bypass AGE_VERIFICATION_REQUIRED if logged in
                # if client.endswith('_agegate') and self._is_unplayable(pr) and self.is_authenticated:
                #     append_client(client.replace('_agegate', '_creator'))
                # elif self._is_agegated(pr):
                #     append_client(client + '_agegate')
                # creator clients can bypass AGE_VERIFICATION_REQUIRED if logged in
                if variant == 'embedded' and self._is_unplayable(pr) and self.is_authenticated:
                    append_client('{}_creator'.format(base_client))
                elif self._is_agegated(pr):
                    if variant == 'tv_embedded':
                        append_client('{}_embedded'.format(base_client))
                    elif not variant:
                        append_client('tv_embedded.{}'.format(base_client), '{}_embedded'.format(base_client))
            if last_error:
                if not len(prs):
                    raise last_error
                self.report_warning(last_error)
            return prs, player_url      
        def build_innertube_clients(self):
            third_party = {
                'embedUrl': 'https://google.com',  # Can be any valid URL
            }
            def qualities(quality_ids):
                """ Get a numeric quality value out of a list of possible values """
                def q(qid):
                    try:
                        return quality_ids.index(qid)
                    except ValueError:
                        return -1
                return q
            base_clients = ('android', 'web', 'ios', 'mweb')
            priority = qualities(base_clients[::-1])
            for client, ytcfg in tuple(INNERTUBE_CLIENTS.items()):
                ytcfg.setdefault('INNERTUBE_API_KEY', 'AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8')
                ytcfg.setdefault('INNERTUBE_HOST', 'www.youtube.com')
                ytcfg.setdefault('REQUIRE_JS_PLAYER', True)
                ytcfg['INNERTUBE_CONTEXT']['client'].setdefault('hl', 'en')
                ytcfg['priority'] = 10 * priority(client.split('_', 1)[0])
                if client in base_clients:
                    import copy
                    INNERTUBE_CLIENTS[client + '_agegate'] = agegate_ytcfg = copy.deepcopy(ytcfg)
                    agegate_ytcfg['INNERTUBE_CONTEXT']['client']['clientScreen'] = 'EMBED'
                    agegate_ytcfg['INNERTUBE_CONTEXT']['thirdParty'] = third_party
                    agegate_ytcfg['priority'] -= 1
                elif client.endswith('_embedded'):
                    ytcfg['INNERTUBE_CONTEXT']['thirdParty'] = third_party
                    ytcfg['priority'] -= 2
                else:
                    ytcfg['priority'] -= 3
        def _extractFormatFromAPI(self, url, webpage, embed_webpage, video_id, age_gate, smuggled_data):
            self.build_innertube_clients()
            master_ytcfg = self.extract_ytcfg(video_id, webpage) or self._get_default_ytcfg()
            player_responses, player_url = self._extract_player_responses(
                self._get_requested_clients(url, smuggled_data), video_id, webpage, master_ytcfg)
            result = []
            for player_response in player_responses:
                try:
                    try:
                        streaming_formats = try_get(player_response, lambda x: x['streamingData']['formats'], list) or []
                        streaming_formats.extend(try_get(player_response, lambda x: x['streamingData']['adaptiveFormats'], list) or [])
                        dashManifestUrl = player_response['streamingData'].get('dashManifestUrl', None)
                    except:
                        streaming_formats = None
                    aResult = self._ExtractFormats(streaming_formats, age_gate, webpage, embed_webpage,video_id, player_url, dashManifestUrl)
                    if aResult:
                        result.extend(aResult)
                except:
                    pass
            return result
        def _extractFormats_spect(self, streaming_formats):
            formats_spec = {}
            for fmt in streaming_formats:
                itag = str_or_none(fmt.get('itag'))
                if not itag:
                    continue
                quality = fmt.get('quality')
                format_note = fmt.get('qualityLabel') or quality
                if format_note == None or format_note=='tiny':
                    format_note = 'DASH audio'                  
                formats_spec[itag] = {
                    'asr': int_or_none(fmt.get('audioSampleRate')),
                    'filesize': int_or_none(fmt.get('contentLength')),
                    'format_note': format_note,
                    'fps': int_or_none(fmt.get('fps')),
                    'height': int_or_none(fmt.get('height')),
                    'tbr': float_or_none(fmt.get('averageBitrate') or fmt.get('bitrate'), 1000) if itag != '43' else None,
                    'width': int_or_none(fmt.get('width')),
                }        
            return formats_spec
        def _signatureURL(self, url, format_id, url_data, age_gate, video_webpage, embed_webpage, video_id):
            if 's' in url_data or self._downloader.params.get('youtube_include_dash_manifest', True):
                ASSETS_RE = [r'"assets":.+?"js":\s*("[^"]+")',
                            r'"jsUrl":("[^"]+")']                        
                jsplayer_url_json = self._search_regex(
                    ASSETS_RE,
                    embed_webpage if age_gate else video_webpage,
                    'JS player URL (1)', default=None)
                if not jsplayer_url_json and not age_gate:
                    # We need the embed website after all
                    if embed_webpage is None:                   
                        embed_url = 'https://www.youtube.com/embed/%s' % video_id
                        embed_webpage = self._download_webpage(
                            embed_url, video_id, 'Downloading embed webpage')
                    jsplayer_url_json = self._search_regex(
                        ASSETS_RE, embed_webpage, 'JS player URL')
                player_url = json.loads(jsplayer_url_json)
                if player_url is None:
                    player_url_json = self._search_regex(
                        r'ytplayer\.config.*?"url"\s*:\s*("[^"]+")',
                        video_webpage, 'age gate player URL')
                    player_url = json.loads(player_url_json)
            if 'sig' in url_data:
                url += '&signature=' + url_data['sig'][0]
            elif 's' in url_data:
                encrypted_sig = url_data['s'][0]
                if self._downloader.params.get('verbose'):
                    if player_url is None:
                        player_version = 'unknown'
                        player_desc = 'unknown'
                    else:
                        if player_url.endswith('swf'):
                            player_version = self._search_regex(
                                r'-(.+?)(?:/watch_as3)?\.swf$', player_url,
                                'flash player', fatal=False)
                            player_desc = 'flash player %s' % player_version
                        else:
                            player_version = self._search_regex(
                                [r'html5player-([^/]+?)(?:/html5player(?:-new)?)?\.js',
                                r'(?:www|player(?:_ias)?)[-.]([^/]+)([^/]+)(?:/[a-z]{2,3}_[A-Z]{2})?/base\.js'],
                                player_url,
                                'html5 player', fatal=False)
                            player_desc = 'html5 player %s' % player_version
                    parts_sizes = self._signature_cache_id(encrypted_sig)
                    self.to_screen('{%s} signature length %s, %s' %
                                    (format_id, parts_sizes, player_desc))
                signature = self._decrypt_signature(
                    encrypted_sig, video_id, player_url, age_gate)
                sp = try_get(url_data, lambda x: x['sp'][0], compat_str) or 'signature'
                url += '&%s=%s' % (sp, signature) 
            return url
        
        
        def update_url_query(self, url, query):
            try:
                import urllib.parse as compat_urlparse
            except ImportError:  # Python 2
                import urlparse as compat_urlparse
            if not query:
                return url
            parsed_url = compat_urlparse.urlparse(url)
            qs = compat_parse_qs(parsed_url.query)
            qs.update(query)
            return compat_urlparse.urlunparse(parsed_url._replace(
                query=compat_urllib_parse_urlencode(qs, True)))
        def _attachMoreFields(self, dct, fmt, formats_spec, formats, url_data):
            video_url = dct['url']
            format_id = dct['format_id']
            if format_id in formats:
                dct.update(formats[format_id])
            if format_id in formats_spec:
                dct.update(formats_spec[format_id])
            mobj = re.search(r'^(?P<width>\d+)[xX](?P<height>\d+)$', url_data.get('size', [''])[0])
            width, height = (int(mobj.group('width')), int(mobj.group('height'))) if mobj else (None, None)
            if width is None:
                width = int_or_none(fmt.get('width'))
            if height is None:
                height = int_or_none(fmt.get('height'))
            def _extract_filesize(media_url):
                return int_or_none(self._search_regex(r'\bclen[=/](\d+)', media_url, 'filesize', default=None))
                                    
            filesize = int_or_none(url_data.get(
                'clen', [None])[0]) or _extract_filesize(video_url)
            quality = url_data.get('quality', [None])[0] or fmt.get('quality')
            quality_label = url_data.get('quality_label', [None])[0] or fmt.get('qualityLabel')
            tbr = (float_or_none(url_data.get('bitrate', [None])[0], 1000)
                    or float_or_none(fmt.get('bitrate'), 1000)) if format_id != '43' else None
            fps = int_or_none(url_data.get('fps', [None])[0]) or int_or_none(fmt.get('fps'))
            format_note = quality_label or quality
            if format_note == None or format_note=='tiny':
                format_note = 'DASH audio'
            more_fields = {
                'filesize': filesize,
                'tbr': tbr,
                'width': width,
                'height': height,
                'fps': fps,
                'format_note': format_note,
            }
            for key, value in more_fields.items():
                if value:
                    dct[key] = value
            if fmt.get('audioTrack') and fmt.get('audioTrack').get('audioIsDefault'):
                dct['isDefaultAudio'] = fmt['audioTrack']['audioIsDefault']
            type_ = url_data.get('type', [None])[0] or fmt.get('mimeType')
            if type_:
                type_split = type_.split(';')
                kind_ext = type_split[0].split('/')
                if len(kind_ext) == 2:
                    kind, _ = kind_ext
                    dct['ext'] = mimetype2ext(type_split[0])
                    if kind in ('audio', 'video'):
                        codecs = None
                        for mobj in re.finditer(
                                r'(?P<key>[a-zA-Z_-]+)=(?P<quote>["\']?)(?P<val>.+?)(?P=quote)(?:;|$)', type_):
                            if mobj.group('key') == 'codecs':
                                codecs = mobj.group('val')
                                break
                        if codecs:
                            dct.update(parse_codecs(codecs))
            if dct.get('acodec') == 'none' or dct.get('vcodec') == 'none':
                CHUNK_SIZE = 10 << 20
                dct.update({
                    'protocol': 'http_dash_segments',
                    'fragments': [{
                        'url': self.update_url_query(dct['url'], {
                            'range': '{}-{}'.format(range_start, min(range_start + CHUNK_SIZE - 1, dct["filesize"]))
                        })
                    } for range_start in range(0, dct['filesize'], CHUNK_SIZE)]
                } if dct['filesize'] else {
                    'downloader_options': {'http_chunk_size': CHUNK_SIZE}  # No longer useful?
                })


        def _fix_n(self, video_url, video_id, player_url):

            query = compat_parse_qs(video_url)
            if query.get('n'):
                try:
                    decrypt_nsig = self._cached(self._decrypt_nsig, 'nsig', query['n'][0])
                    video_url = self.update_url_query(video_url, {
                        'n': decrypt_nsig(query['n'][0], video_id, player_url)
                    })
                except Exception as e:
                    print(e)            
            return video_url

        def _ExtractFormats(self, streaming_formats, age_gate, video_webpage, embed_webpage, video_id, player_url = None, dashManifestUrl=None):                            
            formats = []
            formats_spec = self._extractFormats_spect(streaming_formats)
            itags = []
            for fmt in streaming_formats:
                if fmt.get('drm_families'):
                    continue
                # FORMAT_STREAM_TYPE_OTF(otf=1) requires downloading the init fragment
                # (adding `&sq=0` to the URL) and parsing emsg box to determine the
                # number of fragment that would subsequently requested with (`&sq=N`)                
                if fmt.get('type') == 'FORMAT_STREAM_TYPE_OTF':
                    continue                
                video_url = url_or_none(fmt.get('url'))
                if not video_url:
                    cipher = fmt.get('cipher') or fmt.get('signatureCipher')
                    if not cipher:
                        continue
                    url_data = compat_parse_qs(cipher)
                    video_url = url_or_none(try_get(url_data, lambda x: x['url'][0], compat_str))
                    if not video_url:
                        continue
                else:
                    cipher = None
                    url_data = compat_parse_qs(compat_urllib_parse_urlparse(video_url).query)
                stream_type = int_or_none(try_get(url_data, lambda x: x['stream_type'][0]))
                # Unsupported FORMAT_STREAM_TYPE_OTF
                if stream_type == 3:
                    continue
                format_id = fmt.get('itag') or url_data['itag'][0]
                if not format_id:
                    continue
                format_id = compat_str(format_id)
                if cipher:
                    video_url = self._signatureURL(video_url, format_id, url_data, age_gate, video_webpage, embed_webpage, video_id)
                # if 'ratebypass' not in video_url:
                #     video_url += '&ratebypass=yes'
                video_url = self._fix_n(video_url, video_id, player_url)
                # if self._is_valid_url(video_url, ''):
                #     print('x')
                #     # os._exit(0)
                # else:
                #     print('y')

                dct = {
                    'format_id': format_id,
                    'url': video_url,
                    # 'player_url': player_url,
                }
                self._attachMoreFields(dct, fmt, formats_spec, formats, url_data)
                formats.append(dct) 
                itags.append(format_id)
            get_dash = True
            dash_manifest_url = get_dash and dashManifestUrl
            if dash_manifest_url:
                for f in self._extract_mpd_formats(dash_manifest_url, video_id, fatal=False):
                    itag = f['format_id']
                    if itag in itags:
                        continue
                    if itag:
                        itags.append(itag)
                    # f['quality'] = guess_quality(f)
                    filesize = int_or_none(self._search_regex(
                        r'/clen/(\d+)', f.get('fragment_base_url')
                        or f['url'], 'file size', default=None))
                    if filesize:
                        f['filesize'] = filesize
                    # yield f                  
                    # print(f)
                    # self._attachMoreFields(dct, fmt, formats_spec, formats, url_data)
                    formats.append(f) 
                    itags.append(itag)                    
            return formats
        def _extract_player_info(self, player_url):
            _PLAYER_INFO_RE = (
                r'/s/player/(?P<id>[a-zA-Z0-9_-]{8,})/player',
                r'/(?P<id>[a-zA-Z0-9_-]{8,})/player(?:_ias\.vflset(?:/[a-zA-Z]{2,3}_[a-zA-Z]{2,3})?|-plasma-ias-(?:phone|tablet)-[a-z]{2}_[A-Z]{2}\.vflset)/base\.js$',
                r'\b(?P<id>vfl[a-zA-Z0-9_-]+)\b.*?\.js$',
            )            
            for player_re in _PLAYER_INFO_RE:
                id_m = re.search(player_re, player_url)
                if id_m:
                    break
            else:
                raise ExtractorError('Cannot identify player %r' % player_url)
            return id_m.group('id')                 
        def _NewExtract_signature_function(self, video_id, player_url, example_sig):
            
            player_id = self._extract_player_info(player_url)
            func_id = 'js_%s_%s' % (
                player_id, self._signature_cache_id(example_sig))
            assert os.path.basename(func_id) == func_id
            cache_spec = self._downloader.cache.load('youtube-sigfuncs', func_id)
            if cache_spec is not None:
                return lambda s: ''.join(s[i] for i in cache_spec)
            download_note = (
                'Downloading player %s' % player_url
                if self._downloader.params.get('verbose') else
                'Downloading %s player %s' % (player_type, player_id)
            )
            # if player_type == 'js':
            code = self._download_webpage(
                player_url, video_id,
                note=download_note,
                errnote='Download of %s failed' % player_url)
            res = self._parse_sig_js(code)
            try:
                compat_chr = unichr  # Python 2
            except NameError:
                compat_chr = chr
            test_string = ''.join(map(compat_chr, range(len(example_sig))))
            cache_res = res(test_string)
            cache_spec = [ord(c) for c in cache_res]
            self._downloader.cache.store('youtube-sigfuncs', func_id, cache_spec)
            return res        
        def _extract_signature_function(self, video_id, player_url, example_sig):
            try:
                return self._NewExtract_signature_function(video_id, player_url, example_sig)
            except Exception as ex:
                return super(YoutubeIE, self)._extract_signature_function( video_id, player_url, example_sig)  

        def _extract_n_function_name(self, jscode):
            funcname, idx = self._search_regex(
                r'\.get\("n"\)\)&&\(b=(?P<nfunc>[a-zA-Z0-9$]+)(?:\[(?P<idx>\d+)\])?\([a-zA-Z0-9]\)',
                jscode, 'Initial JS player n function name', group=('nfunc', 'idx'))
            if not idx:
                return funcname

            return json.loads(js_to_json(self._search_regex(
                rf'var {re.escape(funcname)}\s*=\s*(\[.+?\])\s*[,;]', jscode,
                f'Initial JS player n function list ({funcname}.{idx})')))[int(idx)]

        def _extract_n_function_code(self, video_id, player_url):
            player_id = self._extract_player_info(player_url)
            func_code = self.cache.load('youtube-nsig', player_id)
            jscode = func_code or self._load_player(video_id, player_url)
            jsi = CreateJSInterpreterEx(jscode)

            if func_code:
                return jsi, player_id, func_code

            func_name = self._extract_n_function_name(jscode)

            # For redundancy
            func_code = self._search_regex(
                r'''(?xs)%s\s*=\s*function\s*\((?P<var>[\w$]+)\)\s*
                        # NB: The end of the regex is intentionally kept strict
                        {(?P<code>.+?}\s*return\ [\w$]+.join\(""\))};''' % func_name,
                jscode, 'nsig function', group=('var', 'code'), default=None)
            if func_code:
                func_code = ([func_code[0]], func_code[1])
            else:
                self.write_debug('Extracting nsig function with jsinterp')
                func_code = jsi.extract_function_code(func_name)

            self.cache.store('youtube-nsig', player_id, func_code)
            return jsi, player_id, func_code


        def _extract_n_function_code_(self, video_id, player_url):
            player_id = self._extract_player_info(player_url)
            func_code = self.cache.load('youtube-nsig', player_id)
            if func_code:
                return None, player_id, func_code
            jscode = self._load_player(video_id, player_url)
            jscode = jscode.replace('\n', '')
            jsi = CreateJSInterpreterEx(jscode)           
            func_name = self._extract_n_function_name(jscode)

            # For redundancy
            func_code = self._search_regex(
                r'''(?xs)%s\s*=\s*function\s*\((?P<var>[\w$]+)\)\s*
                        # NB: The end of the regex is intentionally kept strict
                        {(?P<code>.+?}\s*return\ [\w$]+.join\(""\))};''' % func_name,
                jscode, 'nsig function', group=('var', 'code'), default=None)
            
            if func_code:
                func_code = (func_code[0], func_code[1])
            # else:
            #     self.write_debug('Extracting nsig function with jsinterp')
            #     func_code = jsi.extract_function_code(func_name)

            self.cache.store('youtube-nsig', player_id, func_code)
            return jsi, player_id, func_code
        
        def _extract_n_function_from_code_(self, jsi, func_code):
            function_name = 'xxyxx'
            js_code = f'function {function_name}({func_code[0]}){{{func_code[1]}}}'
            jsi = CreateJSInterpreterEx(js_code)
            func = jsi.extract_function(function_name)
            return lambda s: func([s])            
            jsi.call_function()
            # func = jsi.extract_function_from_code(*func_code)            
            def extract_nsig(s):
                return jsi.call_function([s])
                # ret = func([s])                
            return extract_nsig    
        
        def _extract_n_function_from_code(self, jsi, func_code):
            func = jsi.extract_function_from_code(*func_code) 
            def extract_nsig(s):
                return func([s])  
            return extract_nsig


        def _decrypt_nsig(self, s, video_id, player_url):
            def urljoin(base, path):
                import urllib.parse as compat_urlparse
                return compat_urlparse.urljoin(base, path)

            """Turn the encrypted n field into a working signature"""
            if player_url is None:
                raise ExtractorError('Cannot decrypt nsig without player_url')
            player_url = urljoin('https://www.youtube.com', player_url)

            try:
                jsi, player_id, func_code = self._extract_n_function_code(video_id, player_url)
            except ExtractorError as e:
                raise ExtractorError('Unable to extract nsig function code', cause=e)
            if self.get_param('youtube_print_sig_code'):
                self.to_screen(f'Extracted nsig function from {player_id}:\n{func_code[1]}\n')

            try:
                extract_nsig = self._cached(self._extract_n_function_from_code, 'nsig func', player_url)
                ret = extract_nsig(jsi, func_code)(s)
            except ExtractorError as e:
                raise ExtractorError('Unable to extract nsig function', cause=e)

            self.write_debug(f'Decrypted nsig {s} => {ret}')
            return ret   

        def _cached(self, func, *cache_id):
            def inner(*args, **kwargs):
                if cache_id not in self._player_cache:
                    try:
                        self._player_cache[cache_id] = func(*args, **kwargs)
                    except ExtractorError as e:
                        self._player_cache[cache_id] = e
                    except Exception as e:
                        import traceback
                        self._player_cache[cache_id] = ExtractorError(traceback.format_exc(), cause=e)

                ret = self._player_cache[cache_id]
                if isinstance(ret, Exception):
                    raise ret
                return ret
            return inner                 

    return YoutubeIE()