import React, { useContext, useEffect, useState } from "react";
import { TreeContext } from "../TreeContext";
import { Chip } from "@mui/material";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import ArrowRightIcon from "@mui/icons-material/ArrowRight";
import TreeView from "@mui/lab/TreeView";
import TreeItem from "@mui/lab/TreeItem";
import Checkbox from "@mui/material/Checkbox";

const PurposeTree = () => {
  const { treeData, handleCheckboxChange } = useContext(TreeContext);
  const [expanded, setExpanded] = useState([]);

  useEffect(() => {
    const getAllNodeIds = (nodes) => {
      return nodes.reduce((acc, node) => {
        return [...acc, node.purpose_id, ...getAllNodeIds(node.children || [])];
      }, []);
    };
    setExpanded(getAllNodeIds(treeData));
  }, [treeData]);

  const renderLabel = (nodeId, label, transformations, selected, disabled) => (
  <div style={{ display: "flex", alignItems: "center" }}>
    <Checkbox
      checked={selected}
      onChange={() => handleCheckboxChange(nodeId)}
      color="primary"
      disabled={disabled}
    />
    <div style={{ color: disabled ? "grey" : "inherit" }}>{label}</div>
    <div style={{ marginLeft: "50px" }}>
      Transformations:
      {transformations.map((transformation) => (
        <Chip key={transformation} label={transformation} color={"primary"} />
      ))}
    </div>
  </div>
);

  const renderTree = (nodes, parentSelected = true) =>
  nodes.map((node) => {
    const disabled = !parentSelected;
    return (
      <TreeItem
        key={node.purpose_id}
        nodeId={node.purpose_id.toString()}
        label={renderLabel(node.purpose_id, node.name, node.transformations, node.selected, disabled)}
      >
        {Array.isArray(node.children) ? renderTree(node.children, node.selected && parentSelected) : null}
      </TreeItem>
    );
  });

  return (
    <TreeView
      defaultCollapseIcon={<ArrowDropDownIcon />}
      defaultExpandIcon={<ArrowRightIcon />}
      defaultExpanded={expanded}
      expanded={expanded}
      multiSelect
    >
      {renderTree(treeData)}
    </TreeView>
  );
};

export default PurposeTree;
