# antdv

## 基础知识

记录一些antdv的使用技巧。

## 任务场景

### 如何使用图标

### 如何替换a-input-search里面的按钮图标icon？
<span id="ainputsearchicon"></span>
默认都是使用放大镜的图标，我想要用FolderOutlined图标，可以这样：

```vue
<a-input-search v-model:value="data.imagesDir" style="width: 400px" @search="handleFolderSelection">
    <template #enterButton>
      <a-button><FolderOutlined /></a-button>
    </template>
</a-input-search>
```

## 常见问题

### 里面的template #enterButton是什么原理？

[参考自定义a-input-search按钮图标的例子](#ainputsearchicon)。
在 Vue 3 中，<template #enterButton> 是使用了 Vue 3 的新特性 —— 具名插槽（Scoped Slots）。
具名插槽允许你更明确地定义和引用插槽内容，使得组件的模板更加清晰和易于理解。
在antdv的a-input-search中，enterButton 是该插槽的名称。在[代码](https://github.com/vueComponent/ant-design-vue/blob/main/components/input/Search.tsx#L92)中可以看到：

```typescript jsx
let { enterButton = slots.enterButton?.() ?? false } = props;
enterButton = enterButton || enterButton === '';
const searchIcon = typeof enterButton === 'boolean' ? <SearchOutlined /> : null;
const btnClassName = `${prefixCls.value}-button`;

const enterButtonAsElement = Array.isArray(enterButton) ? enterButton[0] : enterButton;
let button: any;
const isAntdButton =
    enterButtonAsElement.type &&
    isPlainObject(enterButtonAsElement.type) &&
    enterButtonAsElement.type.__ANT_BUTTON;
if (isAntdButton || enterButtonAsElement.tagName === 'button') {
    button = cloneElement(
        enterButtonAsElement,
        {
            onMousedown,
            onClick: onSearch,
            key: 'enterButton',
            ...(isAntdButton
                ? {
                    class: btnClassName,
                    size: size.value,
                }
                : {}),
        },
        false,
    );
} else {
    const iconOnly = searchIcon && !enterButton;
    button = (
        <Button
            class={btnClassName}
            type={enterButton ? 'primary' : undefined}
            size={size.value}
            disabled={disabled}
            key="enterButton"
            onMousedown={onMousedown}
            onClick={onSearch}  
            loading={loading}
            icon={iconOnly ? searchIcon : null}
        >
            {iconOnly ? null : searchIcon || enterButton}
        </Button>
    );
}
```

可以看到，通过slots.enterButton来提取slot命名插槽值进行处理。
